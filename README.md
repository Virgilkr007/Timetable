# Timetable

This algorithm generates a structured study timetable by taking into account the number of units of each course and its level of importance.

Inputs

The system accepts the following inputs:

i. The number of courses to study

ii. The number of hours available for study per day

iii. The duration of the study period (ranging from 1 week to 1 year)

Course Classification

Each course is classified into one of three status categories:

A – Highly important courses

B – Moderately important courses

C – Least important courses

Classification is based on a combination of course units and importance.

Weighting System
A custom mathematical weighting function is used to assign study time to each course.
Courses with higher priority receive a larger share of the available study slots.

Output
The algorithm generates a timetable that:

Distributes study time proportionally across courses,

Produces a day-by-day study plan for the given period of study.
