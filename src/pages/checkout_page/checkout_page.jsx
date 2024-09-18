import styles from "./checkout_page.module.css";
import logo from "../../images/logo.png";
import arrowGray from "../../images/gray_right_arrow.svg";
import { useNavigate } from "react-router";

const CheckoutPage = () => {
  const navigate = useNavigate();
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <img src={logo} alt="" />
        <div className={styles.backButton} onClick={() => navigate(-1)}>
          <img src={arrowGray} alt="" />
        </div>
      </div>

      <p className={styles.namePageText}>Оформление заказа</p>
      <main>
        <div className={styles.userInfo}>
          <p className={styles.nameText}>Имя Фамилия</p>
          <p className={styles.contactsText}>+7 961 842 40 82</p>
          <p className={styles.contactsText}>kjncks@kmcla.ru</p>
        </div>
        <p className={styles.adressText}>Адрес доставки</p>
        <div className={styles.adressData}>
          <input
            type="text"
            name=""
            id=""
            placeholder="Улица"
            className={styles.street}
          />
          <input
            type="number"
            name=""
            id=""
            placeholder="Квартира"
            className={styles.flat}
          />
          <input
            type="number"
            name=""
            id=""
            placeholder="Этаж"
            className={styles.floor}
          />
          <input
            type="number"
            name=""
            id=""
            placeholder="Подъезд"
            className={styles.entrance}
          />
          <input
            type="text"
            name=""
            id=""
            placeholder="Домофон"
            className={styles.intercom}
          />
          <input
            type="text"
            name=""
            id=""
            placeholder="Комментарий для курьера"
            className={styles.comment}
          />
        </div>
      </main>
    </div>
  );
};

export default CheckoutPage;
