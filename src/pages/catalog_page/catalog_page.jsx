import Header from "../../components/header/header";
import styles from "./catalog_page.module.css";
import filterIcon from "../../images/filter_icon.svg";
import { useState, useEffect } from "react";
import BottomMenu from "../../components/bottom_menu/bottomMenu";
import ProductCard from "../../components/product_card/product_card";
import SortModal from "../../components/sort_modal/sort_modal";
import useWindowDimensions from "../../components/hooks/windowDimensions";
import { getAllBouquetsFull } from "../../components/fetches";

const CatalogPage = () => {
  const [isPressed, setIsPressed] = useState([
    [true],
    [false, false, false, false, false, false],
  ]);
  let copyIsPressed = Array.from(isPressed);
  const { width } = useWindowDimensions();
  const [bouquets, setBouquets] = useState([]);

  const getBouquetsFull = async () => {
    setBouquets(await getAllBouquetsFull());
  };
  useEffect(() => {
    getBouquetsFull();
  }, []);
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.header}>
        <Header />
      </div>
      <p className={styles.namePageText}>Каталог</p>

      <div className={styles.SortFilterButtons}>
        <SortModal />
        <div
          className={styles.filterButton}
          onClick={() => {
            copyIsPressed[0][0] = !copyIsPressed[0][0];
            setIsPressed(copyIsPressed);
          }}
        >
          <img src={filterIcon} alt="" />
        </div>
      </div>

      <div
        className={isPressed[0][0] ? styles.filtersOpen : styles.filtersClose}
      >
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][0]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][0] = !copyIsPressed[1][0];
            setIsPressed(copyIsPressed);
          }}
        >
          Розы
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][1]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][1] = !copyIsPressed[1][1];
            setIsPressed(copyIsPressed);
          }}
        >
          Тюльпаны
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][2]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][2] = !copyIsPressed[1][2];
            setIsPressed(copyIsPressed);
          }}
        >
          Пионы
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][3]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][3] = !copyIsPressed[1][3];
            setIsPressed(copyIsPressed);
          }}
        >
          Орхидеи
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][4]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][4] = !copyIsPressed[1][4];
            setIsPressed(copyIsPressed);
          }}
        >
          Пионы
        </p>
        <p
          className={`${styles.filterButtons} ${
            isPressed[1][5]
              ? styles.activeFilterButton
              : styles.inActiveFilterButton
          }`}
          onClick={() => {
            copyIsPressed[1][5] = !copyIsPressed[1][5];
            setIsPressed(copyIsPressed);
          }}
        >
          Герберы
        </p>
      </div>
      <div className={styles.products}>
        <div className={styles.typeOfBouqets}>
          <p className={styles.nameFilterText}>Летние букеты</p>
          <div className={styles.productsView}>
            {bouquets?.map((elem) => (
              <ProductCard
                name={elem.name}
                price={elem.price}
                uri={elem.url}
                id={elem.id}
              />
            ))}
          </div>
        </div>
      </div>
      <BottomMenu />
    </div>
  );
};

export default CatalogPage;
