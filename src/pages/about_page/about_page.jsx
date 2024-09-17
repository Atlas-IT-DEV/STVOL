import styles from "./about_page.module.css";

import logo from "../../images/logo.png";
import cartIcon from "../../images/cart_icon.svg";
import arrowWhite from "../../images/arrow_white.svg";
import { useState } from "react";

const AboutPage = () => {
  const [isHide, setIsHide] = useState([false, false, false]);
  let copyIsHide = Array.from(isHide);
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <img src={logo} alt="" />
        <div className={styles.cartButton}>
          <img src={cartIcon} alt="" />
        </div>
      </div>
      <div className={styles.infoBlock}>
        <p className={styles.mainInfoText}>
          — сервис доставки цветов <br />
          по Москве, России и миру
        </p>
        <div className={styles.descriptionBlock}>
          <p>
            Мы — служба доставки цветов <br />и подарков по России и миру.
          </p>
          <p>
            У нас вы легко найдёте поздравление <br />
            для любого случая и сможете отправить <br />
            его близким, где бы они не находились.
          </p>
        </div>
      </div>
      <div
        className={styles.buttonShowHide}
        onClick={() => {
          copyIsHide[0] = !copyIsHide[0];
          setIsHide(copyIsHide);
        }}
      >
        <p>Доставка</p>
        <img
          src={arrowWhite}
          alt=""
          className={isHide[0] == false ? styles.arrowDown : styles.arrowUp}
        />
      </div>
      {/* сюда */}
      <div
        className={styles.buttonShowHide}
        onClick={() => {
          copyIsHide[1] = !copyIsHide[1];
          setIsHide(copyIsHide);
        }}
      >
        <p>Доставка</p>
        <img
          src={arrowWhite}
          alt=""
          className={isHide[1] == false ? styles.arrowDown : styles.arrowUp}
        />
      </div>
      {/* сюда */}
      <div
        className={styles.buttonShowHide}
        onClick={() => {
          copyIsHide[2] = !copyIsHide[2];
          setIsHide(copyIsHide);
        }}
      >
        <p>Доставка</p>
        <img
          src={arrowWhite}
          alt=""
          className={isHide[2] == false ? styles.arrowDown : styles.arrowUp}
        />
      </div>
      {/* сюда */}
    </div>
  );
};

export default AboutPage;
