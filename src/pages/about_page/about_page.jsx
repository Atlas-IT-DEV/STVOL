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
      <div className={isHide[0] ? styles.viewOpen : styles.viewClose}>
        <table>
          <tr>
            <th>Интервал</th>
            <th>Москва</th>
            <th>За МКАД</th>
          </tr>
          
          <tr>
            <th>Трехчасовой</th>
            <th>Бесплатно</th>
            <th>399+40₽/км</th>
          </tr>
          <tr>
            <th>Часовой</th>
          </tr>
          <tr>
            <th>Точное время</th>
          </tr>
        </table>
      </div>
      <div
        className={styles.buttonShowHide}
        onClick={() => {
          copyIsHide[1] = !copyIsHide[1];
          setIsHide(copyIsHide);
        }}
      >
        <p>Возврат</p>
        <img
          src={arrowWhite}
          alt=""
          className={isHide[1] == false ? styles.arrowDown : styles.arrowUp}
        />
      </div>
      <div
        className={`${isHide[1] ? styles.viewOpen : styles.viewClose} ${
          styles.deliveryView
        }`}
      >
        <p>
          В соответствии с Законом Российской Федерации «О защите прав
          потребителей» от 07.02.1992 2300-1 (в ред. от 25.10.2007г.) и
          Постановлением Правительства Российской Федерации от 19.01.1998 № 55
          (в ред. 27.03.2007г.) срезанные цветы и горшечные растения обмену и
          возврату не подлежат (Перечень непродовольственных товаров надлежащего
          качества, не подлежащих возврату или обмену). <br />
          <br />
          Покупатель Интернет-магазина имеет право отказаться от получения
          товара в момент его доставки, если доставленный товар ненадлежащего
          качества (на основании п.3 ст. 497 ГК РФ, статья 21 Закона "О защите
          прав потребителей"). Мы заботимся о повышении качества заказов и
          рассматриваем все поступающие претензии в течение 24 часов с момента
          доставки товара. По вопросам, касающимся выполнения заказов, вы можете
          обращаться по электронной почте: ---- или к нам в телеграм: ----
        </p>
      </div>
      <div
        className={styles.buttonShowHide}
        onClick={() => {
          copyIsHide[2] = !copyIsHide[2];
          setIsHide(copyIsHide);
        }}
      >
        <p>Программа лояльности</p>
        <img
          src={arrowWhite}
          alt=""
          className={isHide[2] == false ? styles.arrowDown : styles.arrowUp}
        />
      </div>
      <div className={isHide[2] ? styles.viewOpen : styles.viewClose}>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Repellat
          doloremque doloribus error architecto nostrum, nobis quos delectus,
          nemo soluta aut possimus obcaecati hic eveniet assumenda, animi
          numquam eaque debitis omnis.
        </p>
      </div>
    </div>
  );
};

export default AboutPage;
