import { useState } from "react";
import styles from "./checkout_product_card.module.css";
import bouqet from "../../images/buket1.png";

const CheckoutProductCard = () => {
  const [count, setCount] = useState(1);
  return (
    <div className={styles.container}>
      <div>
        <p className={styles.nameProductText}>STVOL 17</p>
        <p className={styles.descriptionProductText}>Букет из роз и ромашек</p>
        <p className={styles.sumProductText}>{count * 3000} ₽</p>
        <div className={styles.countProduct}>
          <p
            className={styles.selectCountProductText}
            onClick={() => {
              count != 1 ? setCount(count - 1) : setCount(1);
            }}
          >
            -
          </p>
          <p className={styles.countProductText}>{count}</p>
          <p
            className={styles.selectCountProductText}
            onClick={() => {
              setCount(count + 1);
            }}
          >
            +
          </p>
        </div>
      </div>
      <div className={styles.imageProduct}>
        <img src={bouqet} alt="" />
      </div>
    </div>
  );
};
export default CheckoutProductCard;
