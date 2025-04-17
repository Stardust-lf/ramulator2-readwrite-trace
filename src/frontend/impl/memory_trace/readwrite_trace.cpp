#include <filesystem>
#include <fstream>

#include "frontend/frontend.h"
#include "base/exception.h"

namespace Ramulator {

namespace fs = std::filesystem;

class ReadWriteTrace : public IFrontEnd, public Implementation {
  RAMULATOR_REGISTER_IMPLEMENTATION(IFrontEnd, ReadWriteTrace, "ReadWriteTrace", "Read/Write DRAM address vector trace.")

  private:
    struct Trace {
      size_t bubble_count;
      Addr_t addr;
      bool is_write;
    };
    std::vector<Trace> m_trace;
    size_t m_trace_length = 0;
    size_t m_curr_trace_idx = 0;

    size_t m_trace_count = 0;

    Logger_t m_logger;

  public:
    void init() override {
      std::string trace_path_str = param<std::string>("path").desc("Path to the load store trace file.").required();
      m_clock_ratio = param<uint>("clock_ratio").required();

      m_logger = Logging::create_logger("ReadWriteTrace");
      m_logger->info("Loading trace file {} ...", trace_path_str);
      init_trace(trace_path_str);
      m_logger->info("Loaded {} instructions.", m_trace.size());
    };



    void tick() override {
      if (m_curr_trace_idx >= m_trace.size()) {
        return;
      }

      Trace& t = m_trace[m_curr_trace_idx];

      // Skip cycles if bubble_count > 0
      if (t.bubble_count > 0) {
        t.bubble_count--;
        return;
      }

      bool request_sent = m_memory_system->send({t.addr, t.is_write ? Request::Type::Write : Request::Type::Read});
      if (request_sent) {
        m_curr_trace_idx++;
        m_trace_count++;
        // if (m_trace_count % 200000 == 0) {
        //   m_logger->info("Running on instance count {}", m_trace_count);
        // }
      }
    }

  private:
    void init_trace(const std::string& file_path_str) {
      fs::path trace_path(file_path_str);
      if (!fs::exists(trace_path)) {
        throw ConfigurationError("Trace {} does not exist!", file_path_str);
      }

      std::ifstream trace_file(trace_path);
      if (!trace_file.is_open()) {
        throw ConfigurationError("Trace {} cannot be opened!", file_path_str);
      }

      std::string line;
      size_t num_line_insts = 0;
      while (std::getline(trace_file, line)) {
        std::vector<std::string> tokens;
        tokenize(tokens, line, " ");

        int num_tokens = tokens.size();
        if (num_tokens != 3) {
          throw ConfigurationError("Trace {} format invalid!", file_path_str);
        }
        size_t bubble_count = 0;
         if (bubble_count >= 1'000'000) {
          std::cout << "Trace " << file_path_str << " line " << num_line_insts << " bubble count too large!" << std::endl;
        }

        if (bubble_count < 0) {
          std::cout << "Trace " << file_path_str << " line " << num_line_insts << " bubble count negative!" << std::endl;
        }
        bubble_count = std::stoi(tokens[0]);
        bool is_write = tokens[1] == "W";
        Addr_t addr = std::stoll(tokens[2].substr(2), nullptr, 16);
        m_trace.push_back({bubble_count, addr, is_write});

    num_line_insts++;
  }

      trace_file.close();

      m_trace_length = m_trace.size();
    };

    // TODO: FIXME
    bool is_finished() override {
      return m_trace_count >= m_trace_length; 
    };
};

}        // namespace Ramulator
