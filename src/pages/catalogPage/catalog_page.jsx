import BottomMenu from "../../components/bottomMenu";
import styles from "./catalog_page.module.css";
import logo from "../../images/logo.png";
import {
  filterIcon,
  notificationIcon,
  sortedIcon,
  telezhkaIcon,
} from "../../images/images";
import { filter } from "@chakra-ui/react";

const CatalogPage = () => {
  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <img src={logo} alt="" width={141} />
        <div className={styles.headerButtons}>
          <div>{notificationIcon}</div>
          <div>{telezhkaIcon}</div>
        </div>
      </header>
      <main className={styles.mainContent}>
        <p className={`${styles.headersText} ${styles.namePage}`}>Каталог</p>
        <div className={styles.sorted}>
          <div>{filterIcon}</div>
          <div>{sortedIcon}</div>
        </div>
        <div className={styles.filters}>
          <p className={styles.filterButton}>Популярные</p>
          <p className={styles.filterButton}>Акция</p>
          <p className={styles.filterButton}>Сезонные цветы</p>
          <p className={styles.filterButton}>Розы</p>
          <p className={styles.filterButton}>Тюльпаны</p>
          <p className={styles.filterButton}>Пионы</p>
          <p className={styles.filterButton}>Орхидеи</p>
          <p className={styles.filterButton}>Герберы</p>
        </div>
      </main>
      <BottomMenu />
    </div>
  );
};
export default CatalogPage;
