import connexion
import six
import sqlalchemy
import copy

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.training_info import TrainingInfo  # noqa: E501
from swagger_server.models.trainings import Trainings  # noqa: E501
from swagger_server.models.trainings_inner import TrainingsInner
from swagger_server.models.employees_inner import EmployeesInner
from swagger_server.models.employee_info_attend_trainings import EmployeeInfoAttendTrainings
from swagger_server.models.training_info_training_info import TrainingInfoTrainingInfo
from swagger_server.models.trainings import Trainings
from swagger_server import util

#今回は対象外
def delete_trainings_training_id(training_id):  # noqa: E501
    """Delete a training row

    Delete a training row # noqa: E501

    :param training_id: 
    :type training_id: str

    :rtype: None
    """
    return 'do some magic!'

#研修一覧全件取得
def get_trainings():  # noqa: E501
    """Get All trainings

    Get Trainings Lists # noqa: E501


    :rtype: Trainings
    """

    # 接続情報の作成
    engine = sqlalchemy.create_engine(
        'postgresql://waku_db_member:Ljfairmfj@wakupy-db.csw5cdbrfmzu.ap-northeast-1.rds.amazonaws.com/omurice'
    )

    # クエリの作成
    query = 'SELECT * FROM public.m_training'

    #クエリの実行
    result = engine.execute(query)

    #結果を格納するリストの作成
    trainings = []
    training = TrainingsInner()
    
    for row in result:
        training.training_id = row['training_id']
        training.training_name = row['training_name']
        training.training_class = row['training_class']
        training.it_level = row['it_level']
        training.recruitment_num = row['recruitment_numbers']
        training.participation_num = row['participation_numbers']
        training.new_flg = row['new_training_flg']
        training.selection_flg = row['selection_flg']
        training.start_date = row['start_date']
        training.end_date = row['end_date']
        training.skill_class = row['skill_class']

        trainings.append(copy.copy(training))

    #接続クローズ
    result.close()

    #結果をリターン
    return trainings


#研修一覧検索情報取得
def get_trainings_search_results(body=None):  # noqa: E501
    """Search employee&#x27; results

    Get training search results # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Trainings
    """
    if connexion.request.is_json:
        body = Body1().from_dict(connexion.request.get_json())
        #body = Body1.from_dict(connexion.request.get_json())  # noqa: E501


    #接続情報の作成
    engine = sqlalchemy.create_engine(
        'postgresql://waku_db_member:Ljfairmfj@wakupy-db.csw5cdbrfmzu.ap-northeast-1.rds.amazonaws.com/omurice'
    )

    # クエリの作成
    query = "SELECT * FROM public.m_training WHERE 1=1"


    #検索条件にtraining_nameが指定された場合
    if not body.training_name:
        pass
    else:
        query += " AND training_name like '%%{}%%'".format(body.training_name)

    #検索条件にtraining_classが指定された場合(チェックボックス)
    if not body.training_class:
        pass
    else:
        for index, training_class in enumerate(body.training_class):
            if index == 0: 
                query += " AND training_class in ('{}'".format(training_class)
            else:
                query += " ,'{}'".format(training_class)
        
        query += ")"

    #検索条件にskill_classが指定された場合(チェックボックス)
    if not body.skill_class:
        pass
    else:
        for index, skill in enumerate(body.skill_class):
            if index == 0: 
                query += " AND skill_class in ('{}'".format(skill)
            else:
                query += " ,'{}'".format(skill)
        
        query += ")"


    #検索条件にit_levelが指定された場合(チェックボックス)
    if not body.it_level:
        pass
    else:
        for index, it_level in enumerate(body.it_level):
            if index == 0: 
                query += " AND it_level in ('{}'".format(it_level)
            else:
                query += " ,'{}'".format(it_level)
        
        query += ")"

    #検索条件にrecruitment_num_fromが指定された場合
    if not body.recruitment_num_from:
        pass
    else:
        query += " AND recruitment_numbers >= '{}'".format(body.recruitment_num_from)

    #検索条件にrecruitment_num_toが指定された場合
    if not body.recruitment_num_to:
        pass
    else:
        query += " AND recruitment_numbers <= '{}'".format(body.recruitment_num_to)

    #検索条件にnew_flgが指定された場合(チェックボックス)
    if not body.new_flg:
        pass
    else:
        for index, new_flg in enumerate(body.new_flg):
            if index == 0: 
                query += " AND new_training_flg in ('{}'".format(new_flg)
            else:
                query += " ,'{}'".format(new_flg)
        
        query += ")"

        
    #検索条件にselection_flgが指定された場合(チェックボックス)
    if not body.selection_flg:
        pass
    else:
        for index, selection_flg in enumerate(body.selection_flg):
            if index == 0: 
                query += " AND selection_flg in ('{}'".format(selection_flg)
            else:
                query += " ,'{}'".format(selection_flg)
        
        query += ")"


    #検索条件にstart_dateが指定された場合
    if not body.start_date:
        pass
    else:
        query += " AND tstart_date = '{}'".format(body.start_date)

    #検索条件にend_dateが指定された場合
    if not body.end_date:
        pass
    else:
        query += " AND end_date = '{}'".format(body.end_date)


    #クエリの実行
    result = engine.execute(query)
    
    #結果を格納するリストの作成
    trainings = []
    trainings_inner = TrainingsInner()
    
    for row in result:
        trainings_inner.training_name = row['training_name']
        trainings_inner.training_class = row['training_class']
        trainings_inner.skill_class = row['skill_class']
        trainings_inner.it_level = row['it_level']
        trainings_inner.recruitment_num = row['recruitment_numbers']
        trainings_inner.participation_num = row['participation_numbers']
        trainings_inner.new_flg = row['new_training_flg']
        trainings_inner.selection_flg = row['selection_flg']
        trainings_inner.start_date = row['start_date']
        trainings_inner.end_date = row['end_date']

        trainings.append(copy.copy(trainings_inner))

    #接続クローズ
    result.close()

    return trainings

#研修詳細情報取得
def get_trainings_training_id(training_id):  # noqa: E501
    """Get a training info

    Get a training info # noqa: E501

    :param training_id: 
    :type training_id: str

    :rtype: TrainingInfo
    """
    # 接続情報の作成
    engine = sqlalchemy.create_engine(
        'postgresql://waku_db_member:Ljfairmfj@wakupy-db.csw5cdbrfmzu.ap-northeast-1.rds.amazonaws.com/omurice'
    )

    #基本情報の取得
    #クエリの作成
    query = "SELECT * FROM public.m_training WHERE training_id = '{}'".format(training_id)


    #クエリの実行
    result = engine.execute(query)

    training = Body2()
    
    for row in result:
        training.training_id = row['training_id']
        training.training_name = row['training_name']
        training.training_class = row['training_class']
        training.it_level = row['it_level']
        training.summary = row['summary']
        training.recruitment_num = row['recruitment_numbers']
        training.participation_num = row['participation_numbers']
        training.remarks = row['remarks']
        training.num_of_times = row['number_of_times']
        training.time_per_session = row['time_per_session']
        training.new_flg = row['new_training_flg']
        training.selection_flg = row['selection_flg']
        training.start_date = row['start_date']
        training.end_date = row['end_date']
        training.skill_class = row['skill_class']
        training.conditions = row['conditions']
        training.teacher = row['teacher']

    
    #参加社員リストの取得
    #結果を格納するリストの作成
    participating_employees = []

    #クエリの作成
    query = "SELECT * FROM public.t_training_management as T "
    query += "INNER join public.m_employee as M "
    query += "ON T.employee_id = M.employee_id "
    query += "WHERE T.training_id = '{}'".format(training_id)

    #クエリの実行
    result = engine.execute(query)

    training_info = TrainingInfoTrainingInfo()
    
    for row in result:
        training_info.employee_id = row['employee_id']
        training_info.employee_name = row['employee_name']
        training_info.dept = row['dept']
        training_info.joining_year = row['joining_year']
        training_info.title = row['title']
        training_info.grade = row['grade']
        training_info.recruitment_class = row['recruitment_class']
        training_info.attendance_state = row['attendance_state']
        training_info.satisfaction_score = row['satisfaction_score']


        participating_employees.append(copy.copy(training_info))
    
    #接続クローズ
    result.close()

    #結果をリターン
    #return training
    #return participating_employees
    return {"body_2":training,"TrainingInfo_TrainingInfo":participating_employees}

#今回は対象外
def post_trainings_training_id(training_id, body=None):  # noqa: E501
    """Create a training info

    Create a training info # noqa: E501

    :param training_id: 
    :type training_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body2.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
