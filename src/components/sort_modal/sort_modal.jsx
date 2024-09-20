import styles from "./sort_modal.module.css";
import sortIcon from "../../images/sort_icon.svg";
import { useState } from "react";
import { Modal } from "@chakra-ui/react";
import useWindowDimensions from "../hooks/windowDimensions";

const SortModal = () => {
  const [modalVisible, setModalVisible] = useState(false);
  const { width } = useWindowDimensions();
  return (
    <div>
      <div
        className={width >= 500 ? styles.sortButton : styles.sortButton375}
        onClick={() => setModalVisible(true)}
      >
        <img src={sortIcon} alt="" />
      </div>

      {modalVisible && (
        <div className={width >= 500 ? styles.modalView : styles.modalView375}>
          <div className={styles.modalContent}>
            <div className={styles.typesSort}>
              <p className={styles.nameModalText}>Сортировка</p>
              <div className={styles.divideLine} />
              <p className={styles.buttonText}>Cначала дешевле</p>
              <div className={styles.divideLine} />
              <p className={styles.buttonText}>Cначала дороже</p>
            </div>
            <div
              className={styles.cancelButton}
              onClick={() => setModalVisible(false)}
            >
              <p className={styles.buttonText}>Отмена</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default SortModal;
