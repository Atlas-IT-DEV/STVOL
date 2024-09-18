import styles from "./flower_card.module.css";

import flower from "../../images/flower.png";
import useWindowDimensions from "../hooks/windowDimensions";

const FlowerCard = () => {
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375_450}>
      <img src={flower} alt="" className={styles.imageProduct} />
      <p className={styles.nameFlowerText}>Хризантема</p>
      <p className={styles.priceText}>300 ₽</p>
    </div>
  );
};

export default FlowerCard;
