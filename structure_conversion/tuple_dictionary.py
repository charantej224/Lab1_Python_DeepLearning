def sort_tuple():
    student_marks = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)),
                     ('Mark', ('Social', 95)),
                     ('Daniel', ('History', 75)), ('Mark', ('Maths', 100))]
    sorted_marks_directory = {}
    for mark in student_marks:
        if mark[0] in sorted_marks_directory.keys():
            sorted_marks_directory[mark[0]].append(mark[1])
        else:
            sorted_marks_directory[mark[0]] = [mark[1]]

    # Storing values in sorted order
    for key in sorted_marks_directory.keys():
        sorted_marks_directory[key] = sorted(sorted_marks_directory[key])
        print(key, sorted_marks_directory[key])
