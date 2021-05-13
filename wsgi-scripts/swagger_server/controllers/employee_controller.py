import connexion
import six
import sqlalchemy
import copy

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.employee_info import EmployeeInfo  # noqa: E501
from swagger_server.models.employees_inner import EmployeesInner  # noqa: E501
from swagger_server.models.employees import Employees
from swagger_server.models.employee_info_employees_address import EmployeeInfoEmployeesAddress
from swagger_server.models.employee_info_certification_info import EmployeeInfoCertificationInfo
from swagger_server.models.employee_info_attend_trainings import EmployeeInfoAttendTrainings
from swagger_server import util

#社員一覧全件取得
def get_employees():  # noqa: E501
    """Get All employees

    Get Employees Lists # noqa: E501


    :rtype: Employees
    """
    # 接続情報の作成
    engine = sqlalchemy.create_engine(
        'postgresql://waku_db_member:Ljfairmfj@wakupy-db.csw5cdbrfmzu.ap-northeast-1.rds.amazonaws.com/omurice'
    )

    # クエリの作成
    query = 'SELECT * FROM public.m_employee'

    #クエリの実行
    result = engine.execute(query)

    #employees = Employees()
    #結果を格納するリストの作成
    employees = []
    employees_inner = EmployeesInner()
    
    for row in result:
        employees_inner.employee_id = row['employee_id']
        employees_inner.employee_name = row['employee_name']
        #employees_inner.employee_name.decode("unicode-escape")
        #employees_inner.employee_name.encode('unicode-escape')
        #chr(employees_inner.employee_name)
        employees_inner.dept = row['dept']
        employees_inner.joining_year = row['joining_year']
        employees_inner.title = row['title']
        employees_inner.grade = row['grade']
        employees_inner.recruitment_class = row['recruitment_class']
        #employees_inner.leave_flg = row['leave_flg']
        employees_inner.gender = row['gender']
        employees_inner.birthdate = row['birthdate']    

        employees.append(copy.copy(employees_inner))

    #接続クローズ
    result.close()

    #結果をリターン
    return employees
    

#社員詳細情報取得
def get_employees_employee_id(employee_id):  # noqa: E501
    """Get an employee info

    Get an employee info # noqa: E501

    :param employee_id: 
    :type employee_id: str

    :rtype: EmployeeInfo
    """

    # 接続情報の作成
    engine = sqlalchemy.create_engine(
        'postgresql://waku_db_member:Ljfairmfj@wakupy-db.csw5cdbrfmzu.ap-northeast-1.rds.amazonaws.com/omurice'
    )

    #基本情報の取得
    #クエリの作成
    query = "SELECT * FROM public.m_employee WHERE employee_id = '{}'".format(employee_id)

    #クエリの実行
    result = engine.execute(query)

    employees_inner = EmployeesInner()
    employee_address = EmployeeInfoEmployeesAddress()
    
    for row in result:
        employees_inner.employee_id = row['employee_id']
        employees_inner.employee_name = row['employee_name']
        employees_inner.dept = row['dept']
        employees_inner.joining_year = row['joining_year']
        employees_inner.title = row['title']
        employees_inner.grade = row['grade']
        employees_inner.recruitment_class = row['recruitment_class']
        employees_inner.leave_flg = row['leave_flg']
        employees_inner.gender = row['gender']
        employees_inner.birthdate = row['birthdate']
        employee_address.mail_address = row['mailaddress']
        employee_address.company = row['company']

    #研修受講管理の取得
    #結果を格納するリストの作成
    trainings = []

    #クエリの作成
    query = "SELECT * FROM public.t_training_management as T "
    query += "INNER join public.m_training as M "
    query += "ON T.training_id = M.training_id "
    query += "WHERE T.employee_id = '{}'".format(employee_id)

    #クエリの実行
    result = engine.execute(query)

    employee_training = EmployeeInfoAttendTrainings()
    
    for row in result:
        employee_training.training_name = row['training_name']
        employee_training.start_date = row['start_date']
        employee_training.satisfaction_score = row['satisfaction_score']

        trainings.append(copy.copy(employee_training))
    
    #資格情報の取得
    #結果を格納するリストの作成
    certifications= []

    #クエリの作成
    query = "SELECT * FROM public.t_certification_management as T "
    query += "INNER join public.m_certification as M "
    query += "ON T.certification_id = M.certification_id "
    query += "WHERE T.employee_id = '{}'".format(employee_id)

    #クエリの実行
    result = engine.execute(query)

    employee_certification = EmployeeInfoCertificationInfo()
    
    for row in result:
        employee_certification.certification_id = row['certification_id']
        employee_certification.certification_name = row['certification_name']
        employee_certification.get_date = row['get_date']
        employee_certification.summary = row['summary']

        certifications.append(copy.copy(employee_certification))
    
    #接続クローズ
    result.close()

    #結果をリターン
    return {"employees":employees_inner,"employeesAddress":employee_address,"attendTrainings":trainings,"certificationInfo":certifications}


#社員一覧検索情報取得
def get_employees_search_results(body=None):  # noqa: E501
    """Search employee&#x27; results

    Get employee&#x27;s search results # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Employees
    """

    #bodyを取得
    if connexion.request.is_json:
        #body = Body.from_dict(connexion.request.get_json())  # noqa: E501
        body = Body().from_dict(connexion.request.get_json()) 


    #接続情報の作成
    engine = sqlalchemy.create_engine(
        'postgresql://waku_db_member:Ljfairmfj@wakupy-db.csw5cdbrfmzu.ap-northeast-1.rds.amazonaws.com/omurice'
    )

    # クエリの作成
    query = "SELECT * FROM public.m_employee WHERE 1=1"


    #検索条件にemployee_idが指定された場合
    if not body.employee_id:
        pass
    else:
        query += " AND employee_id like '%%{}%%'".format(body.employee_id)

    #検索条件にemployee_nameが指定された場合
    if not body.employee_name:
        pass
    else:
        query += " AND employee_name like '%%{}%%'".format(body.employee_name)

    #検索条件にdeptが指定された場合(チェックボックス)
    if not body.dept:
        pass
    else:
        for index, dept in enumerate(body.dept):
            if index == 0: 
                query += " AND dept in ('{}'".format(dept)
            else:
                query += " ,'{}'".format(dept)
        
        query += ")"

    #検索条件にjoining_year_fromが指定された場合
    if not body.joining_year_from:
        pass
    else:
        query += " AND joining_year >= '{}'".format(body.joining_year_from)

    #検索条件にjoining_year_toが指定された場合
    if not body.joining_year_to:
        pass
    else:
        query += " AND joining_year <= '{}'".format(body.joining_year_to)

    #検索条件にtitleが指定された場合(チェックボックス)
    if not body.title:
        pass
    else:
        for index, title in enumerate(body.title):
            if index == 0: 
                query += " AND title in ('{}'".format(title)
            else:
                query += " ,'{}'".format(title)
        
        query += ")"

        
    #検索条件にgradeが指定された場合(チェックボックス)
    if not body.grade:
        pass
    else:
        for index, grade in enumerate(body.grade):
            if index == 0: 
                query += " AND grade in ('{}'".format(grade)
            else:
                query += " ,'{}'".format(grade)
        
        query += ")"
    
    #検索条件にrecruitment_classが指定された場合(チェックボックス)
    if not body.recruitment_class:
        pass
    else:
        for index, recruitment in enumerate(body.recruitment_class):
            if index == 0: 
                query += " AND recruitment_class in ('{}'".format(recruitment)
            else:
                query += " ,'{}'".format(recruitment)
        
        query += ")"


    #検索条件にleave_flgが指定された場合(チェックボックス)
    if not body.leave_flg:
        pass
    else:
        for index, leave_flg in enumerate(body.leave_flg):
            if index == 0: 
                query += " AND leave_flg in ('{}'".format(leave_flg)
            else:
                query += " ,'{}'".format(leave_flg)
        
        query += ")"

    #検索条件にgenderが指定された場合(チェックボックス)
    if not body.gender:
        pass
    else:
        for index, gender in enumerate(body.gender):
            if index == 0: 
                query += " AND gender in ('{}'".format(gender)
            else:
                query += " ,'{}'".format(gender)
        
        query += ")"

    #検索条件にbirthdate_fromが指定された場合
    if not body.birthdate_from:
        pass
    else:
        query += " AND birthdate >= '{}'".format(body.birthdate_from)

    #検索条件にbirthdate_fromが指定された場合
    if not body.birthdate_to:
        pass
    else:
        query += " AND birthdate <= '{}'".format(body.birthdate_to)


    #クエリの実行
    result = engine.execute(query)
    
    #結果を格納するリストの作成
    employees = []
    employees_inner = EmployeesInner()
    
    for row in result:
        employees_inner.employee_id = row['employee_id']
        employees_inner.employee_name = row['employee_name']
        employees_inner.dept = row['dept']
        employees_inner.joining_year = row['joining_year']
        employees_inner.title = row['title']
        employees_inner.grade = row['grade']
        employees_inner.recruitment_class = row['recruitment_class']
        #employees_inner.leave_flg = row['leave_flg']
        employees_inner.gender = row['gender']
        employees_inner.birthdate = row['birthdate']

        employees.append(copy.copy(employees_inner))

    #接続クローズ
    result.close()

    return employees
