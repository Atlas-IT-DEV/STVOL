import styles from "./flower_card.module.css";
import useWindowDimensions from "../hooks/windowDimensions";

const FlowerCard = ({ image, name, price }) => {
  const { width } = useWindowDimensions();
  return (
    <div className={width >= 500 ? styles.container : styles.container375_450}>
      <img src={image} alt="" className={styles.imageProduct} />
      <p className={styles.nameFlowerText}>{name}</p>
      {price != "-" && <p className={styles.priceText}>{price} ₽</p>}
    </div>
  );
};

export default FlowerCard;
