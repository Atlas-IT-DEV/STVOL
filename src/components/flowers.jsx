import flowers from "../images/buket1.png";
import styles from "./flowers.module.css";

const Flowers = ({
  flower = flowers,
  name = "Букет из роз, фиалок и ромашек",
  price = 3050,
}) => {
  return (
    <div style={{ marginTop: 30 }}>
      <img src={flower} alt="" />
      <p className={styles.nameText}>{name}</p>
      <p className={styles.priceText}>{price} ₽</p>
      <p className={styles.button}>В корзину</p>
    </div>
  );
};

export default Flowers;
