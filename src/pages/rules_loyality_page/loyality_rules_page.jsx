import styles from "./loyality_rules_page.module.css";
import logo from "../../images/logo.png";
import cartIcon from "../../images/cart_icon.svg";
import whiteArrow from "../../images/arrow_white.svg";
import { useNavigate } from "react-router";

const LoyalityRulesPage = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <img src={logo} alt="" />
        <div className={styles.cartButton}>
          <img src={cartIcon} alt="" />
        </div>
      </div>
      <p className={styles.namePageText}>Правила программы лояльности</p>
      <p className={styles.mainText}>
        Регистрация в программе лояльности осуществляется посредством заполнения
        регистрационной формы личного кабинета. <br />
        <br />
        Регистрируясь, пользователь дает свое согласие на участие в программе
        лояльности. Программа лояльности не распространяется на
        незарегистрированных пользователей. <br />
        <br />
        Программа лояльности является накопительной. <br />
        <br />
        Срок действия программы неограничен. <br />
        <br />
        Размер скидки зависит от суммы накоплений: 5% - от 15000 до 49999 рублей
        7% - от 50000 до 74999 рублей 10% - от 75000 до 99999 рублей <br />
        <br />
        В сумме накопительной скидки учитываются все приобретенные ранее товары
        (включая товары со скидками).
        <br />
        <br /> Накопительная скидка не распространяется на акционные товары.
        <br />
        <br />
        Накопительная скидка не распространяется на стоимость доставки. <br />
        <br />
        Интернет-магазин STVOL вправе в одностороннем порядке изменить условия
        или приостановить действие программы лояльности, предварительно
        опубликовав изменения за 10 календарных дней в соответствующем разделе
        сайта.
      </p>

      <div className={styles.backButton} onClick={() => navigate(-1)}>
        <img src={whiteArrow} alt="" />
        <p>Назад</p>
      </div>
    </div>
  );
};

export default LoyalityRulesPage;
