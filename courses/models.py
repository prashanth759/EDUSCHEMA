from django.db import models

class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    CourseDescription = models.TextField(blank=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.CourseName

class Instructor(models.Model):
    InstructorID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Bio = models.TextField(blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    DateOfBirth = models.DateField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Enrollment(models.Model):
    EnrollmentID = models.AutoField(primary_key=True)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    EnrollmentDate = models.DateField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Student} enrolled in {self.Course}"

class Assessment(models.Model):
    AssessmentID = models.AutoField(primary_key=True)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    AssessmentName = models.CharField(max_length=100)
    MaxScore = models.IntegerField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.AssessmentName} for {self.Course}"

class Grade(models.Model):
    GradeID = models.AutoField(primary_key=True)
    Assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Score = models.IntegerField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.Student} scored {self.Score} on {self.Assessment}"

class CourseInstructor(models.Model):
    CourseInstructorID = models.AutoField(primary_key=True)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    AssignmentDate = models.DateField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Instructor} assigned to {self.Course}"
