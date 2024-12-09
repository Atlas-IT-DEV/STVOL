import styles from "./sort_modal.module.css";
import sortIcon from "../../images/sort_icon.svg";
import { useState } from "react";
import { Modal } from "@chakra-ui/react";
import useWindowDimensions from "../hooks/windowDimensions";

const SortModal = ({ ascending, setAscending }) => {
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
              <p
                className={styles.buttonText}
                onClick={() => {
                  setAscending(1);
                  setModalVisible(false);
                }}
              >
                Cначала дешевле
              </p>
              <div className={styles.divideLine} />
              <p
                className={styles.buttonText}
                onClick={() => {
                  setAscending(2);
                  setModalVisible(false);
                }}
              >
                Cначала дороже
              </p>
            </div>
            <div
              className={styles.cancelButton}
              onClick={() => {
                setAscending(0);
                setModalVisible(false);
              }}
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
