import React from 'react';
import '../../../assets/style.css'
import Omurice from '../../../assets/img/omurice.png'
import Cook from '../../../assets/img/cook.png'
import Chick from '../../../assets/img/chick.png'
import { Link } from 'react-router-dom'

export default function MainMenu() {

return (
    <>
        {/* <h2 className="menu-title">メニュー選択(TOP)</h2> */}
        <div className="bg-gray-100 pb-36">
              <div className="container">
                <div>
                  <Link to="/employees"><img src={Cook} className="w-80 h-80 bg-gray-200 rounded-full object-contain"></img></Link>
                  <p className="text-center text-3xl mt-5">社員一覧</p>
                </div>
                <div>
                  <Link to="/trainings"><img src={Omurice} className="w-80 h-80 bg-gray-200 rounded-full object-contain" ></img></Link>
                  <p className="text-center text-3xl mt-5">研修一覧</p>
                </div>
                <div>
                  <Link to="/register"><img src={Chick} className="w-80 h-80 bg-gray-200 rounded-full object-contain" ></img></Link>
                  <p className="text-center text-3xl mt-5">研修登録</p>
                </div>
              </div>
        </div>
    </>
  );
}