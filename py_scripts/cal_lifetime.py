#!/usr/bin/env python3
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

# ------------------------
# 全局参数定义
TOTAL_CACHELINES = 500000  # HBM3 中的总 cacheline 数量
REFRESH_PERIOD = 12         # 刷新周期（小时）
SIMULATION_YEARS = 14       # 模拟总年数
HOURS_PER_YEAR = 8760       # 每年小时数

# 错误类型的 FIT 值（每10亿设备小时的错误次数）
ERROR_FITS = {
    "bit-1": 9000,
    "byte-1": 1500,
    "chip-1": 200
}

# 每种错误类型的永久性错误占比
PERMANENT_ERROR_RATIOS = {
    "bit-1": 0.01,
    "byte-1": 0.01,
    "chip-1": 0.01
}

# SDC 比率相对于 DUE 的系数
SDC_RATIOS = {
    "AMD-chipkill": 5e-3,
    "Green": 1e-4,
    "Bamboo": 7e-7,
    "Green-Bamboo": 3e-8
}

# AMD-chipkill 错误类型概率表
AMD_CHIPKILL = {
    # 基本错误类型
    "bit-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit-2": {"DCE": 0.09768, "DUE": 0.89744, "SDC": 0.00488},
    "bit-3": {"DCE": 0.00997, "DUE": 0.98796, "SDC": 0.00207},
    "bit-4": {"DCE": 0.00097, "DUE": 0.99857, "SDC": 0.00046},
    "bit-5": {"DCE": 0.00011, "DUE": 0.99972, "SDC": 0.00017},
    "bit-6": {"DCE": 0.00001, "DUE": 0.99997, "SDC": 0.00002},
    "bit-7": {"DCE": 0.0, "DUE": 0.99999, "SDC": 0.00001},
    
    "byte-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte-2": {"DCE": 0.08861, "DUE": 0.90770, "SDC": 0.00369},
    "byte-3": {"DCE": 0.00656, "DUE": 0.99193, "SDC": 0.00151},
    "byte-4": {"DCE": 0.00042, "DUE": 0.99918, "SDC": 0.00040},
    "byte-5": {"DCE": 0.00002, "DUE": 0.99988, "SDC": 0.00010},
    "byte-6": {"DCE": 0.0, "DUE": 0.99997, "SDC": 0.00003},
    
    "chip-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    
    # 组合错误类型
    "bit1+byte1": {"DCE": 0.08743, "DUE": 0.90915, "SDC": 0.00342},
    "bit1+byte2": {"DCE": 0.00655, "DUE": 0.99217, "SDC": 0.00128},
    "bit2+byte1": {"DCE": 0.00722, "DUE": 0.99111, "SDC": 0.00167},
    "bit2+byte2": {"DCE": 0.00051, "DUE": 0.99902, "SDC": 0.00047},
    "bit3+byte1": {"DCE": 0.00055, "DUE": 0.99910, "SDC": 0.00035},
    "bit3+byte2": {"DCE": 0.00002, "DUE": 0.99988, "SDC": 0.00010},
    "bit4+byte1": {"DCE": 0.00005, "DUE": 0.99989, "SDC": 0.00006},
    "bit4+byte2": {"DCE": 0.0, "DUE": 0.99996, "SDC": 0.00004},
    "byte2+chip1": {"DCE": 0.0, "DUE": 0.99951, "SDC": 0.00049}
}

# Green 错误类型概率表
GREEN = {
    # 基本错误类型
    "bit-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit-2": {"DCE": 0.88524, "DUE": 0.11476, "SDC": 0.0},
    "bit-3": {"DCE": 0.68563, "DUE": 0.31437, "SDC": 0.0},
    "bit-4": {"DCE": 0.45227, "DUE": 0.54771, "SDC": 0.00002},
    "bit-5": {"DCE": 0.24973, "DUE": 0.75024, "SDC": 0.00003},
    "bit-6": {"DCE": 0.11064, "DUE": 0.88936, "SDC": 0.0},
    "bit-7": {"DCE": 0.03904, "DUE": 0.96094, "SDC": 0.00002},
    "bit-8": {"DCE": 0.01038, "DUE": 0.98958, "SDC": 0.00004},
    
    "byte-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte-2": {"DCE": 0.88591, "DUE": 0.11409, "SDC": 0.0},
    "byte-3": {"DCE": 0.68046, "DUE": 0.31954, "SDC": 0.0},
    "byte-4": {"DCE": 0.43998, "DUE": 0.56002, "SDC": 0.0},
    "byte-5": {"DCE": 0.22909, "DUE": 0.77091, "SDC": 0.0},
    "byte-6": {"DCE": 0.09234, "DUE": 0.90765, "SDC": 0.00001},
    "byte-7": {"DCE": 0.02478, "DUE": 0.97518, "SDC": 0.00004},
    "byte-8": {"DCE": 0.00334, "DUE": 0.99664, "SDC": 0.00002},
    
    "chip-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    
    # 组合错误类型
    "bit1+byte1": {"DCE": 0.88278, "DUE": 0.11722, "SDC": 0.0},
    "bit1+byte2": {"DCE": 0.67990, "DUE": 0.32009, "SDC": 0.00001},
    "bit2+byte1": {"DCE": 0.67896, "DUE": 0.32104, "SDC": 0.0},
    "bit2+byte2": {"DCE": 0.44215, "DUE": 0.55784, "SDC": 0.00001},
    "bit3+byte1": {"DCE": 0.44509, "DUE": 0.55491, "SDC": 0.0},
    "bit3+byte2": {"DCE": 0.23638, "DUE": 0.76362, "SDC": 0.0},
    "bit4+byte1": {"DCE": 0.24314, "DUE": 0.75684, "SDC": 0.00002},
    "bit4+byte2": {"DCE": 0.10036, "DUE": 0.89962, "SDC": 0.00002},
    "byte2+chip1": {"DCE": 0.0, "DUE": 0.99997, "SDC": 0.00003}
}

# Green-Bamboo 错误类型概率表
GREEN_BAMBOO = {
    # 基本错误类型
    "bit-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit-2": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit-3": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit-4": {"DCE": 0.98881, "DUE": 0.01119, "SDC": 0.0},
    "bit-5": {"DCE": 0.95263, "DUE": 0.04737, "SDC": 0.0},
    "bit-6": {"DCE": 0.88287, "DUE": 0.11713, "SDC": 0.0},
    "bit-7": {"DCE": 0.77239, "DUE": 0.22761, "SDC": 0.0},
    
    "byte-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte-2": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte-3": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte-4": {"DCE": 0.98733, "DUE": 0.01267, "SDC": 0.0},
    "byte-5": {"DCE": 0.94716, "DUE": 0.05282, "SDC": 0.00002},
    "byte-6": {"DCE": 0.87060, "DUE": 0.12938, "SDC": 0.00002},
    "byte-7": {"DCE": 0.75178, "DUE": 0.24819, "SDC": 0.00003},
    "byte-8": {"DCE": 0.59378, "DUE": 0.40620, "SDC": 0.00002},
    
    "chip-1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "chip-2": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "chip-3": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    
    # 组合错误类型
    "bit1+byte1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit1+byte2": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit2+byte1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "bit2+byte2": {"DCE": 0.98791, "DUE": 0.01209, "SDC": 0.0},
    "bit3+byte1": {"DCE": 0.98760, "DUE": 0.01240, "SDC": 0.0},
    "bit3+byte2": {"DCE": 0.94953, "DUE": 0.05046, "SDC": 0.00001},
    "bit4+byte1": {"DCE": 0.95101, "DUE": 0.04899, "SDC": 0.0},
    "bit4+byte2": {"DCE": 0.87371, "DUE": 0.12628, "SDC": 0.00001},
    "byte1+chip1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte1+chip2": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte2+chip1": {"DCE": 1.0, "DUE": 0.0, "SDC": 0.0},
    "byte2+chip2": {"DCE": 0.75901, "DUE": 0.24098, "SDC": 0.00001}
}

# ------------------------
# Cacheline 状态类
class CachelineState:
    def __init__(self, error_table):
        self.status = "no_error"   # 初始状态
        self.errors = []           # 存储已注入的错误
        self.error_table = error_table
        self.is_refresh_time = False
    
    def is_terminatable(self):
        # 一旦出现 DUE 或 SDC，状态终止，不再添加新错误
        return self.status in ("DUE", "SDC")
    
    def get_error_combination(self):
        # 统计错误类型数量
        error_counts = {}
        
        for error in self.errors:
            if error["is_permanent"] or not self.is_refresh_time:
                error_type = error["error_type"]
                error_counts[error_type] = error_counts.get(error_type, 0) + 1
        
        # 如果没有错误，返回no_error
        if not error_counts:
            return "no_error"
        
        # 统计基本错误类型数量
        bit_count = 0
        byte_count = 0
        chip_count = 0
        
        for error_type, count in error_counts.items():
            if error_type == "bit-1":
                bit_count += count
            elif error_type == "byte-1":
                byte_count += count
            elif error_type == "chip-1":
                chip_count += count
        
        # 首先尝试确切匹配已知的组合
        # 处理bit+byte组合
        if bit_count == 1 and byte_count == 1:
            key = "bit1+byte1"
            if key in self.error_table:
                return key
        elif bit_count == 1 and byte_count == 2:
            key = "bit1+byte2"
            if key in self.error_table:
                return key
        elif bit_count == 2 and byte_count == 1:
            key = "bit2+byte1"
            if key in self.error_table:
                return key
        elif bit_count == 2 and byte_count == 2:
            key = "bit2+byte2"
            if key in self.error_table:
                return key
        elif bit_count == 3 and byte_count == 1:
            key = "bit3+byte1"
            if key in self.error_table:
                return key
        elif bit_count == 3 and byte_count == 2:
            key = "bit3+byte2"
            if key in self.error_table:
                return key
        elif bit_count == 4 and byte_count == 1:
            key = "bit4+byte1"
            if key in self.error_table:
                return key
        elif bit_count == 4 and byte_count == 2:
            key = "bit4+byte2"
            if key in self.error_table:
                return key
        
        # 处理byte+chip组合
        if byte_count == 1 and chip_count == 1:
            key = "byte1+chip1"
            if key in self.error_table:
                return key
        elif byte_count == 1 and chip_count == 2:
            key = "byte1+chip2"
            if key in self.error_table:
                return key
        elif byte_count == 2 and chip_count == 1:
            key = "byte2+chip1"
            if key in self.error_table:
                return key
        elif byte_count == 2 and chip_count == 2:
            key = "byte2+chip2"
            if key in self.error_table:
                return key
        
        # 如果没有匹配的组合，检查单一错误类型
        if bit_count > 0 and byte_count == 0 and chip_count == 0:
            key = f"bit-{bit_count}"
            if key in self.error_table:
                return key
        
        if byte_count > 0 and bit_count == 0 and chip_count == 0:
            key = f"byte-{byte_count}"
            if key in self.error_table:
                return key
        
        if chip_count > 0 and bit_count == 0 and byte_count == 0:
            key = f"chip-{chip_count}"
            if key in self.error_table:
                return key
        
        # 如果不在表中，直接返回undefined（将被视为DUE）
        return "undefined"
    
    def determine_status(self):
        # 确保不修改终止状态
        if self.is_terminatable() and not self.is_refresh_time:
            return self.status
            
        error_combination = self.get_error_combination()
        
        if error_combination == "no_error":
            return "no_error"
        
        # 处理未定义错误类型
        if error_combination == "undefined":
            # 未定义错误类型默认为DUE
            return "DUE"
        
        # 使用概率确定结果
        percentages = self.error_table[error_combination]
        rand_val = random.random()
        
        if rand_val < percentages["DCE"]:
            return "DCE"
        elif rand_val < percentages["DCE"] + percentages["DUE"]:
            return "DUE"
        else:
            return "SDC"
    
    def refresh(self):
        # 确保DUE和SDC状态在刷新后保持不变
        if self.is_terminatable():
            return
            
        # 刷新周期：仅保留永久性错误
        self.is_refresh_time = True
        self.errors = [e for e in self.errors if e["is_permanent"]]
        # 重新计算状态
        new_status = self.determine_status()
        if new_status == "DCE" or new_status == "no_error":
            self.status = "no_error"
        else:
            self.status = new_status
        self.is_refresh_time = False
    
    def add_error(self, error_type, is_permanent=False):
        if self.is_terminatable():
            return False  # 若已终止，则不再注入错误
        
        self.errors.append({
            "error_type": error_type,
            "is_permanent": is_permanent
        })
        
        # 确定新状态
        new_status = self.determine_status()
        
        # 更新状态（DCE不改变现有状态）
        if new_status == "DUE" or new_status == "SDC":
            self.status = new_status
        
        return True

# ------------------------
# 内存模拟器类
class MemorySimulator:
    def __init__(self, design_name, error_table, total_cachelines=TOTAL_CACHELINES, 
                 error_fits=ERROR_FITS, permanent_ratios=PERMANENT_ERROR_RATIOS, 
                 refresh_period=REFRESH_PERIOD):
        self.design_name = design_name
        self.error_table = error_table
        self.total_cachelines = total_cachelines
        self.error_fits = error_fits
        self.permanent_ratios = permanent_ratios
        self.refresh_period = refresh_period
        self.affected_cachelines = {}  # 只跟踪已受影响的cacheline
        
        # 统计记录
        self.due_counts = []
        self.time_points = []
    
    def calculate_error_probs(self, time_step_hours):
        # 计算每种错误类型在给定时间步内的概率
        probs = {}
        for error_type, fit in self.error_fits.items():
            hourly_rate = fit / 1e9
            probs[error_type] = 1 - math.exp(-hourly_rate * time_step_hours)
        return probs
    
    def run_simulation(self, total_years=SIMULATION_YEARS, time_step_hours=12):
        total_hours = total_years * HOURS_PER_YEAR
        total_steps = int(total_hours / time_step_hours)
        yearly_steps = int(HOURS_PER_YEAR / time_step_hours)
        
        progress_bar = tqdm(total=total_steps, ncols=100, desc=f"{self.design_name} 模拟")
        for step in range(total_steps):
            current_hour = step * time_step_hours
            current_year = current_hour / HOURS_PER_YEAR
            
            # 记录年度统计数据
            if step % yearly_steps == 0:
                due_count = sum(1 for state in self.affected_cachelines.values() if state.status == "DUE")
                due_rate = due_count / self.total_cachelines
                
                self.due_counts.append(due_rate)
                self.time_points.append(current_year)
                progress_bar.set_description(f"{self.design_name} [年份: {current_year:.2f}, DUE: {due_count}]")
            
            # 注入新错误并立即检查
            error_probs = self.calculate_error_probs(time_step_hours)
            for error_type, prob in error_probs.items():
                expected = self.total_cachelines * prob
                actual = np.random.poisson(expected)
                for _ in range(actual):
                    cid = random.randint(0, self.total_cachelines - 1)
                    if cid not in self.affected_cachelines:
                        self.affected_cachelines[cid] = CachelineState(self.error_table)
                    is_perm = random.random() < self.permanent_ratios.get(error_type, 0.5)
                    self.affected_cachelines[cid].add_error(error_type, is_perm)
            
            # 刷新 - 由于现在时间步长等于刷新周期，所以每步都刷新
            for cid in list(self.affected_cachelines.keys()):
                state = self.affected_cachelines[cid]
                state.refresh()
                if state.status == "no_error" and not state.errors:
                    del self.affected_cachelines[cid]
            
            progress_bar.update(1)
        
        progress_bar.close()
        return self.time_points, self.due_counts

def calculate_sdc_rates(design_name, due_rates):
    """根据给定的DUE率计算SDC率"""
    if design_name in SDC_RATIOS:
        return [due * SDC_RATIOS[design_name] for due in due_rates]
    else:
        # 默认使用AMD-chipkill的比率
        return [due * SDC_RATIOS["AMD-chipkill"] for due in due_rates]

def plot_results(designs_data, save_filename='combined_results.png'):
    # Create a figure with two subplots for DUE and SDC
    fig, axs = plt.subplots(2, 1, figsize=(12, 12))
    
    # Set colors and markers
    colors = {
        'AMD-chipkill': '#FF0000', 
        'Green': '#D95319', 
        'Bamboo': '#77AC30',
        'Green-Bamboo': '#0072BD'
    }
    markers = {
        'AMD-chipkill': 's', 
        'Green': 'o', 
        'Bamboo': '^',
        'Green-Bamboo': 'v'
    }
    
    # Set line width and marker size
    linewidth = 2
    markersize = 8
    
    # Plot DUE rates - start from year 1 but keep x-axis from 0
    for design_name, data in designs_data.items():
        # Find the index where time is >= 1
        start_idx = next((i for i, t in enumerate(data['time_points']) if t >= 1), 0)
        
        # Only plot data from year 1 and later
        axs[0].semilogy(
            data['time_points'][start_idx:], 
            data['due_counts'][start_idx:],
            marker=markers.get(design_name, 'o'),
            color=colors.get(design_name, 'black'),
            markersize=markersize,
            linestyle='-', 
            linewidth=linewidth,
            label=design_name
        )
    
    # Configure DUE subplot
    axs[0].set_title('DUE Probability', fontsize=16, fontweight='bold')
    axs[0].set_ylabel('Probability', fontsize=14, fontweight='bold')
    
    # Set custom y-ticks to avoid intermediate values between 10^-6 and 10^-5
    custom_yticks = [1e0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    axs[0].set_yticks(custom_yticks)
    axs[0].set_yticklabels(['10$^0$', '10$^{-1}$', '10$^{-2}$', '10$^{-3}$', '10$^{-4}$', '10$^{-5}$', '10$^{-6}$'])
    
    axs[0].set_ylim(1e-6, 1.05)
    axs[0].set_xlim(0, SIMULATION_YEARS)  # Keep x-axis starting at 0
    axs[0].set_xticks(range(0, SIMULATION_YEARS + 1, 1))
    axs[0].grid(True, which="major", ls="-", alpha=0.2)
    axs[0].legend(loc='upper left')
    
    # Plot SDC rates with the same approach
    for design_name, data in designs_data.items():
        # Find the index where time is >= 1
        start_idx = next((i for i, t in enumerate(data['time_points']) if t >= 1), 0)
        
        # Calculate SDC rates based on DUE rates
        sdc_counts = calculate_sdc_rates(design_name, data['due_counts'])
        
        # Only plot data from year 1 and later
        axs[1].semilogy(
            data['time_points'][start_idx:], 
            sdc_counts[start_idx:],
            marker=markers.get(design_name, 'o'),
            color=colors.get(design_name, 'black'),
            markersize=markersize,
            linestyle='-', 
            linewidth=linewidth,
            label=design_name
        )
    
    # Configure SDC subplot
    axs[1].set_title('SDC Probability', fontsize=16, fontweight='bold')
    axs[1].set_ylabel('Probability', fontsize=14, fontweight='bold')
    
    # Set custom y-ticks for SDC plot
    custom_yticks_sdc = [1e0, 1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12]
    axs[1].set_yticks(custom_yticks_sdc)
    axs[1].set_yticklabels(['10$^0$', '10$^{-2}$', '10$^{-4}$', '10$^{-6}$', '10$^{-8}$', '10$^{-10}$', '10$^{-12}$'])
    
    axs[1].set_ylim(1e-12, 1.05)
    axs[1].set_xlim(0, SIMULATION_YEARS)  # Keep x-axis starting at 0
    axs[1].set_xticks(range(0, SIMULATION_YEARS + 1, 1))
    axs[1].grid(True, which="major", ls="-", alpha=0.2)
    axs[1].legend(loc='upper left')
    
    # Add x-axis label (only on bottom subplot)
    axs[1].set_xlabel('Time (Years)', fontsize=14, fontweight='bold')
    
    # Disable minor ticks which might create intermediate marks between powers of 10
    axs[0].minorticks_off()
    axs[1].minorticks_off()
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(save_filename, dpi=300)
    plt.show()

# ------------------------
# 主函数
def main():
    start_time = time.time()
    print("当前模拟配置:")
    print(f"总cacheline数: {TOTAL_CACHELINES}")
    print(f"刷新周期: {REFRESH_PERIOD}小时")
    print(f"模拟总年数: {SIMULATION_YEARS}年")
    print("\n错误FIT率和永久性错误占比:")
    for etype in ERROR_FITS:
        print(f"{etype:<10} FIT: {ERROR_FITS[etype]:<5} 永久性错误占比: {PERMANENT_ERROR_RATIOS[etype]:.2f}")
    print("\nSDC与DUE概率比率:")
    for design, ratio in SDC_RATIOS.items():
        print(f"{design:<12} SDC/DUE 比率: {ratio:.1e}")
    print()
    
    designs_data = {}
    
    # Bamboo会使用AMD-chipkill的表，但SDC率使用自己的系数
    designs = [
        {"name": "AMD-chipkill", "table": AMD_CHIPKILL},
        {"name": "Green", "table": GREEN},
        {"name": "Bamboo", "table": AMD_CHIPKILL},  # 使用AMD-chipkill的表
        {"name": "Green-Bamboo", "table": GREEN_BAMBOO}
    ]
    
    # 同时进行所有设计的模拟
    for design in designs:
        print(f"\n开始 {design['name']} 模拟...")
        simulator = MemorySimulator(
            design_name=design["name"],
            error_table=design["table"],
            total_cachelines=TOTAL_CACHELINES,
            error_fits=ERROR_FITS,
            permanent_ratios=PERMANENT_ERROR_RATIOS,
            refresh_period=REFRESH_PERIOD
        )
        
        t_points, due_counts = simulator.run_simulation(
            total_years=SIMULATION_YEARS,
            time_step_hours=12  # 直接使用刷新周期作为时间步长
        )
        
        designs_data[design["name"]] = {
            "time_points": t_points,
            "due_counts": due_counts
        }
        
        # 计算SDC率
        sdc_rates = calculate_sdc_rates(design["name"], due_counts)
        
        print(f"{design['name']} 最终 DUE 率: {due_counts[-1]:.10f}")
        print(f"{design['name']} 最终 SDC 率: {sdc_rates[-1]:.10e}")
    
    # 生成组合图表
    print("\n生成设计比较图表...")
    print(designs_data)
    # plot_results(designs_data, save_filename='memory_protection_comparison.png')
    
    print("\n模拟完成!")
    print(f"总计 {SIMULATION_YEARS} 年模拟时间")
    print(f"模拟 {TOTAL_CACHELINES} 个cacheline")
    
    elapsed = time.time() - start_time
    print(f"\n总运行时间: {elapsed:.2f} 秒")

if __name__ == "__main__":
    main()
