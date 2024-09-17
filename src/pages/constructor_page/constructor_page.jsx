import BottomMenu from "../../components/bottom_menu/bottomMenu";
import Header from "../../components/header/header";
import SelectFlower from "../../components/select_flower/select_flower";
import styles from "./constructor_page.module.css";

const ConstructorPage = () => {
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <Header />
      </div>
      <p className={styles.namePageText}>Конструктор</p>

      <div className={styles.bouquetContainer}>
        <p>Ваш букет появится здесь</p>
      </div>
      <div className={styles.addButton}>
        <p>В корзину</p>
      </div>
      <div className={styles.flowerSelect}>
        <SelectFlower />
      </div>
      <p className={styles.helpText}>
        Подсказка:
        <span>
          {" "}
          свайпни влево для того,
          <br /> чтобы перейти к настройке букета
        </span>
      </p>
      <BottomMenu />
    </div>
  );
};

export default ConstructorPage;
