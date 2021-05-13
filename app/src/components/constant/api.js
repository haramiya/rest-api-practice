const ROOT_URL = "http://172.22.128.121"

export const API_ENDPOINT = {

    // 社員一覧ALL取得API
    EMPLOYEES_ALL: `${ROOT_URL}/employees`,
    // 社員検索API
    EMPLOYEES_SEARCH: `${ROOT_URL}/employees/search`,
    // 社員詳細API
    EMPLOYEES_INFO: `${ROOT_URL}/employees/:employeeId`,

    // 研修一覧ALL取得API
    TRAININGS_ALL: `${ROOT_URL}/trainings`,
    // 研修検索API
    TRAININGS_SEARCH: `${ROOT_URL}/trainings/search`,
    // 研修詳細API
    TRAININGS_INFO: `${ROOT_URL}/trainings/:trainingId`,
     // 研修登録API
    TRAININGS_REGISTER: `${ROOT_URL}/trainings/register`,

}