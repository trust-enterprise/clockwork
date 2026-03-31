import matplotlib.pyplot as plt

# pie chart
import matplotlib.pyplot as plt

activities = ["Study", "Play", "Sleep"]
hours = [5, 3, 8]

plt.pie(hours, labels=activities)
plt.title("My Daily Routine")

plt.show()


# bar chart
subjects = ["Maths", "Science", "English"]
marks = [80, 70, 90]

plt.bar(subjects, marks)
plt.title("My Exam Marks")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.show()
