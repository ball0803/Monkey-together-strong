def sign_in(uid, sid, exam_info):
    if not any(uid == seen[0] or sid == seen[1] for seen in exam_info): exam_info.append([uid, sid, [], [], 0])
def get_welcome_and_rules_msg():
    return 'ยินดีต้อนรับสู่การสอบกลางภาคครับ\n\nอยากแนะนำว่า อย่าเอาเปรียบเพื่อนเลยนะครับ ความทรงจำช่วงวัยรุ่นจะอยู่กับเราไปอีกนาน\n\nขอให้ทำข้อสอบได้ทุกคนครับ'
def get_student_info(uid, exam_info):
    return [student for student in exam_info if student[0] == uid][0]
def get_question(uid, exam_info, all_questions):
    exam_info[exam_info.index(get_student_info(uid, exam_info))][2].append([q for q in all_questions if q not in get_student_info(uid, exam_info)[2]][random.randint(0, len(all_questions) - len(get_student_info(uid, exam_info)[2]) - 1)]) if len(get_student_info(uid, exam_info)[2]) < len(all_questions) else None
def submit_answer(uid, answer, exam_info):
    exam_info[exam_info.index(get_student_info(uid, exam_info))][3].append(answer) 
    exam_info[exam_info.index(get_student_info(uid, exam_info))][4] += 1
