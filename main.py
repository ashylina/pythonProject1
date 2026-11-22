import customtkinter as ctk

# 1. 主题和颜色
ctk.set_appearance_mode("System")  # 模式跟随系统
ctk.set_default_color_theme("blue")  # 蓝色主题

# 2. 主窗口
app = ctk.CTk()
app.title("Ashylina's To-Do List")  # 窗口标题
app.geometry("400x600")  # 设置窗口大小 宽400，高500

# 3. 添加一个简单的欢迎标签（Label）
welcome_label = ctk.CTkLabel(app, text="Welcome！", font=("Arial", 20))
welcome_label.pack(pady=20)  # pady=20 是上下留白，让它别贴边

# 5. 顶部标 签
title_label = ctk.CTkLabel(app, text="MY TO-DO LIST",
                           font=("Arial", 20, "bold"),
                           text_color="#2C3E50")
title_label.pack(pady=(20, 10))

# 输入框
task_entry = ctk.CTkEntry(app, width=300, height=40,
                          placeholder_text="Enter a Task",
                          corner_radius=40, )
task_entry.pack(pady=20)


# 定义按钮后的执行函数
def add_task():
    task_text = task_entry.get()  # 输入内容后
    # 若不为空
    if task_text != "":
        print("ok", task_text)
    task_entry.delete(0, "end")


# 按钮设置
add_button = ctk.CTkButton(app,
                           text="Add Task",
                           width=150, height=40,
                           font=("Arial", 20, "bold"),
                           fg_color="#2C3E50",
                           command=add_task)
# 添加按钮
add_button.pack(pady=20)

app.mainloop()  # 循环
