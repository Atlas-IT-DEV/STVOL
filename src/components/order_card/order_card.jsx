import styles from "./order_card.module.css";

import bouqet from "../../images/buket1.png";
import grayArrowRight from "../../images/gray_right_arrow.svg";
import useWindowDimensions from "../hooks/windowDimensions";

const OrderCard = () => {
  const {width} = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <img src={bouqet} alt="" />
      <p className={styles.dateText}>06.08.2024</p>
      <div className={styles.orderButton}>
        <p>STVOL 18</p>
        <img src={grayArrowRight} alt="" />
      </div>
    </div>
  );
};

export default OrderCard;
