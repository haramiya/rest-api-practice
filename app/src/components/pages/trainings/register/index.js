import React from "react";
import axios from "axios";
import { useForm } from "react-hook-form";
import { TRAINING_CONST } from "../../../constant/training";
import { API_ENDPOINT } from "../../../constant/api";
// import Button from "@material-ui/core/Button";
import SearchButton from "../../../templates/Button"
import TextBox from "../../../templates/TextBox"
import TextArea from "../../../templates/TextArea"
import Calendar from "../../../templates/Calendar"
import RadioButton from "../../../templates/RadioButton"
import SearchHeader2 from "../../../templates/SearchHead2"

const TrainingsRegister = (props) => {

    // ref属性がregisterがであるものを監視
    const { register, handleSubmit } = useForm();

    // 登録ボタン押下時の処理
    const onSubmit = (data) => {

        const params = JSON.stringify(data);

        // 登録成功／失敗メッセージ表示エリアの取得
        var elm = document.getElementById('insertMessage');

        window.confirm('この内容を登録しますか？')

        axios({
                method: "POST",
                url: API_ENDPOINT.TRAININGS_REGISTER,
                data: params,
                headers: { "Content-Type": "application/json; charset=utf-8" },
            }).then((res) => {
                console.log("click register button");
                console.log(res)
                elm.textContent = '登録に成功しました';
                elm.style.color = "green"
            }).catch(err => {
                console.log(err)
                elm.textContent = '登録に失敗しました';
                elm.style.color = "red"
            });
    };

    // 研修分類チェックボックスのループ処理
    const inputTrainingClass = Object.entries(TRAINING_CONST.trainingClass).map(
        ([key, trainingClass]) => (
            <RadioButton register={register} name="trainingClass" value={key} text={trainingClass}/>
        )
    );

    // スキル分類チェックボックスのループ処理
    const inputSkillClass = Object.entries(TRAINING_CONST.skillClass).map(
        ([key, skillClass]) => (
            <RadioButton register={register} name="skillClass" value={key} text={skillClass}/>
        )
    );

    // ITレベルチェックボックスのループ処理
    const inputITLevel = Object.entries(TRAINING_CONST.ITLevel).map(
        ([key, ITLevel]) => (
            <RadioButton register={register} name="ITLevel" value={key} text={ITLevel}/>
        )
    );

    // 既存/新規チェックボックスのループ処理
    const inputNewFlg = Object.entries(TRAINING_CONST.newFlg).map(
        ([key, newFlg]) => (
            <RadioButton register={register} name="newFlg" value={key} text={newFlg} required="required"/>
        )
    );

    // 選抜/募集のループ処理
    const inputSelectionFlg = Object.entries(TRAINING_CONST.selectionFlg).map(
        ([key, selectionFlg]) => (
            <RadioButton register={register} name="selectionFlg" value={key} text={selectionFlg} required="required"/>
        )
    );

    return (
        <>
            <div className="bg-gray-100 flex flex-col xs:flex-row items-center xs:justify-between">
                <form onSubmit={handleSubmit(onSubmit)}>
                <table className="border-gray-200 shadow-lg">
                    <caption className="text-gray-700 text-3xl font-medium font-bol pt-8 pb-5">研修登録</caption>
                    {/* <!---研修ID---> */}
                    <tr>
                        <td className="border-b border-gray-200 bg-gray-200 text-gray-600 w-auto text-center">研修ID<label className="text-red-400"> ※</label></td>
                        <TextBox register={register} name="trainingId" required="required" maxLength="7"/>
                    </tr>
                    {/* <!---研修名---> */}
                    <tr>
                        <td className="border-b border-gray-200 bg-gray-200 text-gray-600 w-auto text-center">研修名<label className="text-red-400"> ※</label></td>
                        <TextBox register={register} name="trainingName" required="required"/>
                    </tr>
                    {/* <!---研修分類---> */}
                    <tr>
                        <SearchHeader2 text="研修分類"/>
                        <td className="border-b border-gray-200 bg-white">{inputTrainingClass}</td>
                    </tr>
                    {/* <!---スキル分類---> */}
                    <tr>
                        <SearchHeader2 text="スキル分類"/>
                        <td className="border-b border-gray-200 bg-white">{inputSkillClass}</td>
                    </tr>
                    {/* <!---IT人材レベル--->                         */}
                    <tr>
                        <SearchHeader2 text="IT人材レベル"/>
                        <td className="border-b border-gray-200 bg-white">{inputITLevel}</td>
                    </tr>
                    {/* <!---概要--->*/}
                    <tr>
                        <SearchHeader2 text="概要"/>
                        <TextArea register={register} name="summary" rows="4" cols="40"/>
                    </tr>
                    {/* <!---募集人数---> */}
                    <tr>
                        <SearchHeader2 text="募集人数"/>
                        <td className="border-b border-gray-200 bg-white">
                            <input type="number" className="ml-3 border-2 border-gray-200 rounded-md" name="recruitmentNum" ref={register} ></input>
                        </td>
                    </tr>
                    {/* <!---参加人数---> */}
                    <tr>
                        <SearchHeader2 text="参加人数"/>
                        <td className="border-b border-gray-200 bg-white">
                            <input type="number" className="ml-3 border-2 border-gray-200 rounded-md" name="participationNum" ref={register} ></input>
                        </td>
                    </tr>
                    {/* <!---概要--->*/}
                    <tr>
                        <SearchHeader2 text="備考"/>
                        <TextArea register={register} name="summary" rows="4" cols="40"/>
                    </tr>
                    {/* <!---研修開始・終了---> */}
                    <tr>
                        <SearchHeader2 text="研修開始日"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Calendar register={register} name="startDate" />
                        </td>
                    </tr>
                    <tr>
                        <SearchHeader2 text="研修終了日"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Calendar register={register} name="endDate" />
                        </td>
                    </tr>
                    {/* <!---実施回数---> */}
                    <tr>
                        <SearchHeader2 text="実施回数"/>
                        <td className="border-b border-gray-200 bg-white">
                            <input type="number" className="ml-3 border-2 border-gray-200 rounded-md" name="numOfTimes" ref={register} ></input>
                        </td>
                    </tr>
                    {/* <!---1回あたりの時間---> */}
                    <tr>
                        <SearchHeader2 text="1回あたりの時間"/>
                        <td className="border-b border-gray-200 bg-white">
                            <input type="number" className="ml-3 border-2 border-gray-200 rounded-md" name="timePerSession" ref={register} ></input>
                        </td>
                    </tr>
                    {/* <!---新規/既存---> */}
                    <tr>
                        <td className="border-b border-gray-200 bg-gray-200 text-gray-600 w-auto text-center">新規/既存<label className="text-red-400"> ※</label></td>
                        <td className="border-b border-gray-200 bg-white" >{inputNewFlg}</td>
                    </tr>
                    {/* <!---選抜/募集---> */}
                    <tr>
                        <td className="border-b border-gray-200 bg-gray-200 text-gray-600 w-auto text-center">選抜/募集<label className="text-red-400"> ※</label></td>
                        <td className="border-b border-gray-200 bg-white">{inputSelectionFlg}</td>
                    </tr>
                    {/* <!---参加条件--->*/}
                    <tr>
                        <SearchHeader2 text="参加条件"/>
                        <TextArea register={register} name="conditions" rows="2" cols="40"/>
                    </tr>
                    {/* <!---主催会社--->*/}
                    <tr>
                        <SearchHeader2 text="主催会社"/>
                        <TextBox register={register} name="company"/>
                    </tr>
                    {/* <!---講師名--->*/}
                    <tr>
                        <SearchHeader2 text="講師名"/>
                        <TextBox register={register} name="teacher"/>
                    </tr>
                </table>
                {/* <!---登録ボタン押下するとメッセージをボタン上部に表示する---> */}
                <div id="insertMessage" className="text-center pt-5 text-red-500 text-xl"></div>
                <div className="pt-2 ml-96">
                    <SearchButton className="ml-5" text="登録"/>
                </div>
                </form>
            </div>
            <div className="bg-gray-100 pl-96 pb-5">
                {/* <Button size="large" variant="outlined" color="secondary" component={Link} onClick={() => history.goBack()}>戻る</Button> */}
            </div>
        </>
    )
}

export default TrainingsRegister