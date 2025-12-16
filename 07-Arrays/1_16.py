distances_traveled = [120, 150, 180, 90, 200, 175, 160]
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
file_names = [
    "report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
    "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"
]

sorted_distances = sorted(distances_traveled)
print("Distances (low to high):", sorted_distances)

sorted_temperatures = sorted(daily_temperatures, reverse=True)
print("Temperatures (high to low):", sorted_temperatures)

sorted_files = sorted(file_names)
print("File names (ascending):", sorted_files)