import Header from "../../components/header/header";
import BottomMenu from "../../components/bottom_menu/bottomMenu";
import styles from "./profile_page.module.css";

import grayArrowRight from "../../images/gray_right_arrow.svg";
import OrderSlider from "../../components/order_slider/order_slider";
import { useStores } from "../../store/store_context";

const ProfilePage = ({ status = "Бронзовый ствол — 5%" }) => {
  const { pageStore } = useStores();
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <Header />
      </div>
      <p className={styles.namePageText}>Профиль</p>

      <div className={styles.profileInfo}>
        {/* <div className={styles.editButton}>
          <p>Редактировать</p>
          <img src={grayArrowRight} alt="" />
        </div> */}
        <p className={styles.nameProfileText}>{pageStore.name}</p>
        <p className={styles.phoneNumberText}>+7 961 842 40 82</p>
      </div>
      <p className={styles.statusLoyalityText}>Статус программы лояльности</p>
      <div className={styles.statusView}>
        <p>{status}</p>
      </div>
      <p className={styles.orderText}>Заказы</p>
      <div className={styles.orders}>
        <OrderSlider />
      </div>

      <BottomMenu />
    </div>
  );
};

export default ProfilePage;
