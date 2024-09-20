import styles from "./about_page.module.css";

import logo from "../../images/logo.svg";
import cartIcon from "../../images/cart_icon.svg";
import arrowWhite from "../../images/arrow_white.svg";
import tgIcon from "../../images/tg_icon.svg";
import whatsappIcon from "../../images/whatsapp_icon.svg";
import emaiIcon from "../../images/mail_icon.svg";

import { useState } from "react";
import BottomMenu from "../../components/bottom_menu/bottomMenu";
import { useNavigate } from "react-router";
import useWindowDimensions from "../../components/hooks/windowDimensions";

const AboutPage = () => {
  const [isHide, setIsHide] = useState([false, false, false]);
  let copyIsHide = Array.from(isHide);
  const navigate = useNavigate();
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.header}>
        <img src={logo} alt="" />
        <div className={styles.cartButton} onClick={() => navigate("/cart")}>
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
      <main>
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
            <tr
              style={{
                color: "rgba(55, 55, 55, 1)",
                fontSize: 20,
                fontFamily: "TTNorms500",
              }}
            >
              <td>Интервал</td>
              <td>Москва</td>
              <td>За МКАД</td>
            </tr>

            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                borderBottom: "1px solid rgba(55, 55, 55, 1)",
                height: 45,
              }}
            >
              <td>Трехчасовой</td>
              <td>Бесплатно</td>
              <td>399+40₽/км</td>
            </tr>
            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                borderBottom: "1px solid rgba(55, 55, 55, 1)",
                height: 45,
              }}
            >
              <td>Часовой</td>
              <td>499 ₽</td>
              <td>699+40₽/км</td>
            </tr>
            <tr
              style={{
                color: "rgba(156, 156, 156, 1)",
                fontFamily: "TTNorms400",
                fontSize: 20,
                height: 45,
              }}
            >
              <td>Точное время</td>
              <td>999 ₽</td>
              <td>1199+40₽/км</td>
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
            возврату не подлежат (Перечень непродовольственных товаров
            надлежащего качества, не подлежащих возврату или обмену). <br />
            <br />
            Покупатель Интернет-магазина имеет право отказаться от получения
            товара в момент его доставки, если доставленный товар ненадлежащего
            качества (на основании п.3 ст. 497 ГК РФ, статья 21 Закона "О защите
            прав потребителей"). Мы заботимся о повышении качества заказов и
            рассматриваем все поступающие претензии в течение 24 часов с момента
            доставки товара. По вопросам, касающимся выполнения заказов, вы
            можете обращаться по электронной почте: ---- или к нам в телеграм:
            ----
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
        <div
          className={`${isHide[2] ? styles.viewOpen : styles.viewClose} ${
            styles.loyalityView
          }`}
        >
          <div>
            <div className={styles.descriptionLoyality}>
              <p className={styles.nameText}>Бронзовый STVOL</p>
              <p className={styles.discountText}>5%</p>
            </div>
            <p className={styles.priceText}>15 000 ₽ - 49 999 ₽</p>
          </div>
          <div>
            <div className={styles.descriptionLoyality}>
              <p className={styles.nameText}>Серебряный STVOL</p>
              <p className={styles.discountText}>7%</p>
            </div>
            <p className={styles.priceText}>50 000 ₽ - 74 999 ₽</p>
          </div>
          <div>
            <div className={styles.descriptionLoyality}>
              <p className={styles.nameText}>Золотой STVOL</p>
              <p className={styles.discountText}>10%</p>
            </div>
            <p className={styles.priceText}>75 000 ₽ - 100 000 ₽</p>
          </div>
          <p
            className={styles.rulesText}
            onClick={() => navigate("/loyality_rules")}
          >
            Правила лояльности
          </p>
        </div>
      </main>
      <div className={styles.footer}>
        <div className={styles.aboutCompany}>
          <div>
            <p className={styles.attributeCompanyText}>ИП</p>
            <p className={styles.valueCompanyText}>ИП Алиев Али Рауф Оглы</p>
          </div>
          <div>
            <p className={styles.attributeCompanyText}>ОКВЭД</p>
            <p className={styles.valueCompanyText}>ИП STVOL букет</p>
          </div>
          <div>
            <p className={styles.attributeCompanyText}>ИНН</p>
            <p className={styles.valueCompanyText}>34567865436</p>
          </div>
        </div>
        <div className={styles.aboutCompany}>
          <div className={styles.tgButton}>
            <img src={tgIcon} alt="" />
            <p>@STVOL</p>
          </div>
          <div className={styles.phoneButton}>
            <img src={whatsappIcon} alt="" />
            <p>+7 927 927 43 53</p>
          </div>
          <div className={styles.emailButton}>
            <img src={emaiIcon} alt="" />
            <p>bhewfj@jfj.ru</p>
          </div>
        </div>
      </div>

      <BottomMenu />
    </div>
  );
};

export default AboutPage;
