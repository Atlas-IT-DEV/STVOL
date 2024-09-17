import Header from "../../components/header/header";
import styles from "./catalog_page.module.css";

const CatalogPage = () => {
  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <Header />
      </div>
    </div>
  );
};

export default CatalogPage;
