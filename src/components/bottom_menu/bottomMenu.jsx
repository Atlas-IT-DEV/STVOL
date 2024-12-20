import { useState } from "react";
import constructorIcon from "../../images/constructor_icon.svg";
import profileIcon from "../../images/profile_icon.svg";
import catalogIcon from "../../images/catalog_icon.svg";
import logo from "../../images/logo.png";
import { useNavigate } from "react-router";
import styles from "./bottomMenu.module.css";
import useWindowDimensions from "../hooks/windowDimensions";
import { useToast } from "@chakra-ui/react";
import { VStack, Text } from "@chakra-ui/react";

const BottomMenu = () => {
  const [isActive, setIsActive] = useState([0, 0, 1, 0]);
  const navigate = useNavigate();
  const { width } = useWindowDimensions();
  const toast = useToast();
  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <div className={styles.button} onClick={() => navigate("/profile")}>
        <img src={profileIcon} alt="" className={styles.profileIcon} />
        <p>Профиль</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/")}>
        <img src={catalogIcon} alt="" className={styles.catalogIcon} />
        <p>Каталог</p>
      </div>
      <div
        className={styles.button}
        onClick={() => {
          navigate("/constructor");
          toast({
            render: () => (
              <VStack
                color="white"
                p={3}
                bg="black"
                borderRadius={"12px"}
                border={"2px solid #c81768"}
              >
                <Text color={"white"}>Конструктор в разработке</Text>
              </VStack>
            ),
            duration: 1500,
            isClosable: true,
            position: "top",
          });
        }}
      >
        <img src={constructorIcon} width={43} />
        <p>Конструктор</p>
      </div>
      <div className={styles.button} onClick={() => navigate("/about")}>
        <img src={logo} width={97} />
        <p>О нас</p>
      </div>
    </div>
  );
};

export default BottomMenu;
