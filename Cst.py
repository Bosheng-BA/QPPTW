import os
import airport
# 打开并读取文件
DATA_PATH = "/Users/小巴的工作台/BBS_WORK_SPACE/Python_Workspace/airport/Datas/DATA"
APT_FILE = os.path.join(DATA_PATH, "tianjin_new.txt")

airc_file_name = "/Users/小巴的工作台/BBS_WORK_SPACE/Python_Workspace/Dynamic_Routing/airport/Datas/traffic/acft_types.txt"

flight_file_name = "/Users/小巴的工作台/BBS_WORK_SPACE/Python_Workspace/Dynamic_Routing/airport/Datas/traffic/gaptraffic-2017-08-03-new.csv"

# 存储文件的位置

# 确保目录存在
file = 'saved_figures_gaptraffic-2019-08-07-new'
os.makedirs(file, exist_ok=True)

# points = main.the_airport2.points
