import React from 'react';
import MenuLogo from '../../assets/img/menu-button.png'
import OmuriceLogo from '../../assets/img/omurice_header.png'

export default function Header() {

  return (
    <>
      <div className="border-b-2 bg-white">
      <header className="mx-auto flex justify-between">
      <div className="page-header my-5">
        <h1 className="">
          <a className="float-left" href="">
            <img className="h-20" src={OmuriceLogo} alt="メニュー選択"></img>
          </a>
          <div className="float-left text-4xl text-center my-3 font-bold">　×　 </div>
          <a className="float-left" href="">
            <img className="h-20" src={OmuriceLogo} alt="メニュー選択"></img>
          </a>
        </h1>
        </div>
        <div className="flex float-right">
        {/* <div className="right"> */}
          <div className="flex float-right mr-10 my-5">ユーザー名</div>
            <div><button className="flex float-right mr-10 my-3 bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded shadow-lg">
                    ログアウト
            </button></div>
          <div className="float-right mr-5 my-4"><img src={MenuLogo} alt="メニューボタン" width="30" height="25" /></div>
        </div>
      </header>
      </div>
    </>
  );
}