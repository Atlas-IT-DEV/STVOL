import styles from "./flower_card.module.css";

import flower from "../../images/flower.png"

const FlowerCard = () => {
  return (
    <div className={styles.container}>
      <img
        src={flower}
        alt=""
        className={styles.imageProduct}
      />
      <p className={styles.nameFlowerText}>Хризантема</p>
      <p className={styles.priceText}>300 ₽</p>
    </div>
  );
};

export default FlowerCard;
