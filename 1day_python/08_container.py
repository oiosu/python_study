name = 'su'
name1 = 'ku'
name2 = 'na'
name3 = 'ha'
name4 = 'ja'
name5 = 'us'

# 리스트
# 다양한 값들의 나열
students = ['su', 'ku', 'na', 'ha', 'ja', 'us']
# 인덱스 순서로 접근 
print(students[0]) #su 
print (students[-1]) #us

# 1회차, 2회차, 3회차 나눠서 학생들을 나눠서 작성해 본다면?
students_1 = ['su', 'ku']
students_2 = ['na', 'ha']
students_3 = ['ja', 'us']

# 딕셔너리 
# 키-값의 쌍
students = {
    '1회차': ['su', 'ku'], 
    '2회차' : ['na', 'ha'], 
    '3회차' : ['ja', 'us']
    }

# 키로 접근 
print(students['1회차'])