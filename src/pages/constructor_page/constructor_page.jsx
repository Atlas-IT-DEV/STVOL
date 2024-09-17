import BottomMenu from "../../components/bottom_menu/bottomMenu";
import Header from "../../components/header/header";
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
      <BottomMenu />
    </div>
  );
};

export default ConstructorPage;
