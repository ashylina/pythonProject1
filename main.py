import customtkinter as ctk

# 1. 主题和颜色
ctk.set_appearance_mode("Light")  # 模式跟随系统
ctk.set_default_color_theme("dark-blue")  # 主题色

# 2. 主窗口
app = ctk.CTk()
app.title("Ashylina's To-Do List")  # 窗口标题
app.geometry("400x600")  # 窗口大小

# 3. 添加一个简单的欢迎标签（Label）
welcome_label = ctk.CTkLabel(app, text="Welcome！", font=("Arial", 20))
welcome_label.pack(pady=20)  # pady上下留白

# 5. 顶部标 签
title_label = ctk.CTkLabel(app, text="MY TO-DO LIST",
                           font=("Arial", 20, "bold"),
                           text_color="#1E3A1E")
title_label.pack(pady=(20, 10))

# 输入框
task_entry = ctk.CTkEntry(app, width=300, height=40,
                          placeholder_text="Enter a Task",
                          corner_radius=40, )
task_entry.pack(pady=20)
# 创建栏目(背景板
task_list_frame = ctk.CTkScrollableFrame(app, width=10, height=10, fg_color="#E8F0DC", corner_radius=30)
task_list_frame.pack(pady=10, fill="both", expand=True)


# 定义按钮后的执行函数
task_labels = []


def add_task():
    task_text = task_entry.get()  # 输入内容后
    # 若不为空
    if task_text != "":
        # 标签
        task_card = ctk.CTkFrame(task_list_frame, fg_color="#B8C9A0", corner_radius=10, width=330, height=40)

        # 标签大小
        task_card.pack_propagate(False)
        task_card.grid(row=len(task_labels), column=0, padx=10, pady=10, sticky="ew")
        # 标签显示
        label = ctk.CTkLabel(task_card, text="· " + task_text, font=("Arial", 20), anchor="w")
        label.pack(side=ctk.LEFT, pady=10)
        task_labels.append(label)
        task_entry.delete(0, "end")

# 设置任务标签


# 按钮设置
add_button = ctk.CTkButton(app,
                           text="Add Task",
                           width=150, height=40,
                           font=("Arial", 20, "bold"),
                           fg_color="#4A6B6A",
                           command=add_task)
# 添加按钮
add_button.pack(pady=20)

app.mainloop()  # 循环
