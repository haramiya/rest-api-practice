import React from "react";
import axios from "axios";
import { useForm } from "react-hook-form";
import { TRAINING_CONST } from "../../../constant/training";
import { API_ENDPOINT } from "../../../constant/api";
import SearchButton from "../../../templates/Button"
import TextBox from "../../../templates/TextBox"
import Calendar from "../../../templates/Calendar"
import Checkbox from "../../../templates/CheckBox.js"
import SearchHeader from "../../../templates/SearchHead"

const TrainingsSearch = (props) => {

    // ref属性がregisterがであるものを監視
    const { register, handleSubmit } = useForm();

    // 検索ボタン押下時の処理
    const onSubmit = (data) => {

        //数値型に変換
        data.recruitmentNumFrom = Number(data.recruitmentNumFrom);
        data.recruitmentNumTo = Number(data.recruitmentNumTo);

        // 不要なパラメータ削除
        for (const key in data) {
            if (data[key] == "" || data[key] ===  null) {
                delete data[key];
            }
        }

        // 入力値をJSON形式に変換
        const params = JSON.stringify(data);

        // API処理
        axios({
                method: "POST",
                url: API_ENDPOINT.TRAININGS_SEARCH,
                data: params,
                headers: { "Content-Type": "application/json; charset=utf-8" },
            }).then((res) => {
                console.log("click search button");
                console.log(res.data);
                props.changeTrainings(res.data);
            });
    };

    // 研修分類チェックボックスのループ処理
    const inputTrainingClass = Object.entries(TRAINING_CONST.trainingClass).map(
        ([key, trainingClass]) => (
            <Checkbox register={register} name="trainingClass" value={key} text={trainingClass}/>
        )
    );

    // スキル分類チェックボックスのループ処理
    const inputSkillClass = Object.entries(TRAINING_CONST.skillClass).map(
        ([key, skillClass]) => (
            <Checkbox register={register} name="skillClass" value={key} text={skillClass}/>
        )
    );

    // ITレベルチェックボックスのループ処理
    const inputITLevel = Object.entries(TRAINING_CONST.ITLevel).map(
        ([key, ITLevel]) => (
            <Checkbox register={register} name="ITLevel" value={key} text={ITLevel}/>
        )
    );

    // 既存/新規チェックボックスのループ処理
    const inputNewFlg = Object.entries(TRAINING_CONST.newFlg).map(
        ([key, newFlg]) => (
            <Checkbox register={register} name="newFlg" value={key} text={newFlg}/>
        )
    );

    // 選抜/募集のループ処理
    const inputSelectionFlg = Object.entries(TRAINING_CONST.selectionFlg).map(
        ([key, selectionFlg]) => (
            <Checkbox register={register} name="selectionFlg" value={key} text={selectionFlg}/>
        )
    );

    return (
        <>
            <div className="bg-gray-100 flex flex-col xs:flex-row items-center xs:justify-between">
                <form onSubmit={handleSubmit(onSubmit)}>
                <table className="border-gray-200 shadow-lg">
                    {/* <!---研修名---> */}
                    <tr>
                        <SearchHeader text="研修名"/>
                        <TextBox register={register} name="trainingName"/>
                    </tr>
                    {/* <!---研修分類---> */}
                    <tr>
                        <SearchHeader text="研修分類"/>
                        <td className="border-b border-gray-200 bg-white">{inputTrainingClass}</td>
                    </tr>
                    {/* <!---スキル分類---> */}
                    <tr>
                        <SearchHeader text="スキル分類"/>
                        <td className="border-b border-gray-200 bg-white">{inputSkillClass}</td>
                    </tr>
                    {/* <!---IT人材レベル--->                         */}
                    <tr>
                        <SearchHeader text="IT人材レベル"/>
                        <td className="border-b border-gray-200 bg-white">{inputITLevel}</td>
                    </tr>
                    {/* <!---募集人数---> */}
                    <tr>
                        <SearchHeader text="募集人数"/>
                        <td className="border-b border-gray-200 bg-white">
                            <input type="number" className="ml-3 border-2 border-gray-200 rounded-md" name="recruitmentNumFrom" ref={register} ></input>
                            　～　
                            <input type="number" className="ml-3 border-2 border-gray-200 rounded-md" name="recruitmentNumTo" ref={register} ></input>
                        </td>
                    </tr>
                    {/* <!---新規/既存---> */}
                    <tr>
                        <SearchHeader text="既存/新規"/>
                        <td className="border-b border-gray-200 bg-white">{inputNewFlg}</td>
                    </tr>
                    {/* <!---選抜/募集---> */}
                    <tr>
                        <SearchHeader text="選抜/募集"/>
                        <td className="border-b border-gray-200 bg-white">{inputSelectionFlg}</td>
                    </tr>
                    {/* <!---研修開始・終了---> */}
                    <tr>
                        <SearchHeader text="研修開始日"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Calendar register={register} name="startDate" />
                        </td>
                    </tr>
                    <tr>
                        <SearchHeader text="研修終了日"/>
                        <td className="border-b border-gray-200 bg-white">
                            <Calendar register={register} name="endDate" />
                        </td>
                    </tr>
                </table>
                <div className="py-5 ml-96">
                    <SearchButton/>
                </div>
                </form>
            </div>
        </>
    )
}

export default TrainingsSearch