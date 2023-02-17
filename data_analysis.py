import pandas as pd
import scipy.stats as stat
import matplotlib as mpl
import matplotlib.pyplot as plt
import os


BASE_DIRECTORY = os.getcwd()

# Splitting the hard test results from the regular test results for each task
data0 = pd.read_csv(BASE_DIRECTORY + "/stat/std_data.csv", index_col = None)
data1 = data0[data0["Test_Type"].str.contains("hard")]
data0= data0[data0["Test_Type"].str.contains("test")]

data2 = pd.read_csv(BASE_DIRECTORY + "/stat/ET2_data.csv", index_col = None)
data2h = data2[data2["Test_Type"].str.contains("hard")]
data2 = data2[data2["Test_Type"].str.contains("test")]

data3 = pd.read_csv(BASE_DIRECTORY + "/stat/ET3_data.csv", index_col = None)
data3h = data3[data3["Test_Type"].str.contains("hard")]
data3 = data3[data3["Test_Type"].str.contains("test")]

# --------- Average and Standard Deviation ---------
fig, ax = plt.subplots(nrows = 3, ncols = 2, sharex = True, figsize = (12,10))

x_vals = ("Standard Code", "ET 1", "ET 2", "ET 3")

y_vals = [data0["Number of clauses"].mean(), data1["Number of clauses"].mean(), data2["Number of clauses"].mean(), data3["Number of clauses"].mean()]

plot = ax[0,0].bar(x_vals,y_vals, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

ax[0,0].set_ylabel("Number of Clauses")
ax[0,0].set_title("Average Number of Clasuses in each Task")
ax[0,0].bar_label(plot, label_type = "center")
ax[0,0].text(0.001, 0.99, "a)", transform = ax[0,0].transAxes, verticalalignment = "top")

y_vals = [data0["Number of clauses"].std(), data1["Number of clauses"].std(), data2["Number of clauses"].std(), data3["Number of clauses"].std()]

plot = ax[0,1].bar(x_vals,y_vals, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

#ax[0,1].set_ylabel("Number of Clauses")
ax[0,1].set_title("Standard Deviation Number of Clasuses in each Task")
ax[0,1].bar_label(plot, label_type = "center")
ax[0,1].text(0.001, 0.99, "b)", transform = ax[0,1].transAxes, verticalalignment = "top")

y_vals = [data0["Memory used"].mean(), data1["Memory used"].mean(), data2["Memory used"].mean(), data3["Memory used"].mean()]

plot = ax[1,0].bar(x_vals,y_vals, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

ax[1,0].set_ylabel("Memory Used (MB)")
ax[1,0].set_title("Average Memory Usage in each Task")
ax[1,0].bar_label(plot, label_type = "center")
ax[1,0].text(0.001, 0.99, "c)", transform = ax[1,0].transAxes, verticalalignment = "top")

y_vals = [data0["Memory used"].std(), data1["Memory used"].std(), data2["Memory used"].std(), data3["Memory used"].std()]

plot = ax[1,1].bar(x_vals,y_vals, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

#ax[1,1].set_ylabel("Memory Used (MB)")
ax[1,1].set_title("Standard Deviation of Memory Used in each Task")
ax[1,1].bar_label(plot, label_type = "center")
ax[1,1].text(0.001, 0.99, "d)", transform = ax[1,1].transAxes, verticalalignment = "top")

y_vals = [data0["CPU time"].mean(), data1["CPU time"].mean(), data2["CPU time"].mean(), data3["CPU time"].mean()]

plot = ax[2,0].bar(x_vals,y_vals, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

ax[2,0].set_xlabel("Task ID")
ax[2,0].set_ylabel("CPU Time (s)")
ax[2,0].set_title("Average CPU Time in each Task")
ax[2,0].bar_label(plot, label_type = "center")
ax[2,0].text(0.001, 0.99, "e)", transform = ax[2,0].transAxes, verticalalignment = "top")

y_vals = [data0["CPU time"].std(), data1["CPU time"].std(), data2["CPU time"].std(), data3["CPU time"].std()]

plot = ax[2,1].bar(x_vals,y_vals, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

ax[2,1].set_xlabel("Task ID")
#ax[2,1].set_ylabel("CPU Time (s)")
ax[2,1].set_title("Standard Deviation of CPU Time in each Task")
ax[2,1].bar_label(plot, label_type = "center")
ax[2,1].text(0.001, 0.99, "f)", transform = ax[2,1].transAxes, verticalalignment = "top")

plt.subplots_adjust(left = 0.075, right = 0.975, top = 0.95, bottom = 0.05)

fig.savefig('./report/images/average_std.png')

#plt.show()

# --------- End Of Average and Standard Deviation ---------

# --------- Worst Case Scenario ---------

max_clause_count = [data0["Number of clauses"].max(), data1["Number of clauses"].max(), data2["Number of clauses"].max(), data3["Number of clauses"].max()]

max_memory_used = [data0["Memory used"].max(), data1["Memory used"].max(), data2["Memory used"].max(), data3["Memory used"].max()]

max_cpu_time = [data0["CPU time"].max(), data1["CPU time"].max(), data2["CPU time"].max(), data3["CPU time"].max()]

fig2, ax2 = plt.subplots(nrows = 3, ncols = 1, sharex = True, figsize = (6,8))

plot = ax2[0].bar(x_vals, max_clause_count, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

ax2[0].set_ylabel("Number of Clauses")
ax2[0].set_title("Worst Case Number of Clauses")
ax2[0].bar_label(plot, label_type = "center")
ax2[0].text(0.001, 0.99, "a)", transform = ax2[0].transAxes, verticalalignment = "top")
plot = ax2[1].bar(x_vals, max_memory_used, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

ax2[1].set_ylabel("Memory Used (MB)")
ax2[1].set_title("Worst Case Memory Usage")
ax2[1].bar_label(plot, label_type = "center")
ax2[1].text(0.001, 0.99, "b)",  transform = ax2[1].transAxes, verticalalignment = "top")

plot = ax2[2].bar(x_vals, max_cpu_time, color = ["#DAD7CD", "#A3B18A", "#588157", "#3A5A40"])

ax2[2].set_xlabel("Task ID")
ax2[2].set_ylabel("CPU Time (s)")
ax2[2].set_title("Worst Case CPU Time")
ax2[2].bar_label(plot, label_type = "center")
ax2[2].text(0.001, 0.99, "c)",  transform = ax2[2].transAxes, verticalalignment = "top")

plt.subplots_adjust(right = 0.95, top = 0.95, bottom = 0.07)

fig2.savefig("./report/images/worst_case.png")

#plt.show()

# --------- End Of Worst Case Scenario ---------
