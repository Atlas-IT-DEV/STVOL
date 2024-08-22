import BottomBenu from "../../components/bottomMenu";
import { notificationIcon, telezhkaIcon } from "../../images/images";
import styles from "./profile_page.module.css";
import logo from "./../../images/logo.png";
import Order from "../../components/order";

const ProfilePage = ({
  name = "Фамилия Имя",
  phone_number = "+7 800 555 35 35",
  bronze = "5%",
  silver = "10%",
  gold = "15%",
  bonus = 115,
  adress = "Москва, ул. Арбат, д. 36",
}) => {
  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <img src={logo} alt="" width={141} />
        <div className={styles.headerButtons}>
          <div>{notificationIcon}</div>
          <div>{telezhkaIcon}</div>
        </div>
      </header>
      <main className={styles.mainInfo}>
        <div className={styles.profile}>
          <p className={`${styles.headerProfile} ${styles.mainTextColor}`}>
            Профиль
          </p>
          <p className={`${styles.editButton} ${styles.mainTextColor}`}>
            Редактировать
          </p>
          <p className={`${styles.nameText} ${styles.mainTextColor}`}>{name}</p>
          <p className={`${styles.phoneText} ${styles.mainTextColor}`}>
            {phone_number}
          </p>
          <p className={`${styles.attributes} ${styles.mainTextColor}`}>
            Бронзовый ствол
          </p>
          <div className={styles.discountField}>
            <p
              className={`${styles.values} ${styles.bronzeDiscount} ${styles.fieldPadding}`}
            >
              {bronze}
            </p>
            <p
              className={`${styles.values} ${styles.silverDiscount} ${styles.fieldPadding}`}
            >
              {silver}
            </p>
            <p
              className={`${styles.values} ${styles.goldDiscount} ${styles.fieldPadding}`}
            >
              {gold}
            </p>
          </div>
          <p className={`${styles.attributes} ${styles.mainTextColor} `}>
            Бонусы
          </p>
          <div className={styles.bonusField}>
            <p
              className={`${styles.values} ${styles.fieldValue} ${styles.fieldPadding}`}
            >
              {bonus}
            </p>
          </div>
          <p className={`${styles.attributes} ${styles.mainTextColor}`}>
            Адрес
          </p>
          <div className={styles.adressField}>
            <p
              className={`${styles.values} ${styles.fieldValue} ${styles.fieldPadding}`}
            >
              {adress}
            </p>
          </div>
        </div>
        <div className={styles.orders}>
          <p
            className={`${styles.values} ${styles.fieldValue} ${styles.fieldPadding}`}
          >
            Заказы
          </p>
          <div className={styles.historyOrders}>
            <Order />
            <Order />
            <Order />
            <Order />
          </div>
        </div>
      </main>
      <BottomBenu />
    </div>
  );
};
export default ProfilePage;
