import styles from "./product_card.module.css";
import { Swiper, SwiperSlide } from "swiper/react";
// Import Swiper styles
import "swiper/css";
import "swiper/css/pagination";
import { VStack, Hstack, Text, HStack } from "@chakra-ui/react";

// import "swiper/css/navigation";
import { FreeMode, Pagination } from "swiper/modules";
import { useNavigate } from "react-router";
import useWindowDimensions from "../hooks/windowDimensions";
import { useStores } from "../../store/store_context";
import { background, useToast } from "@chakra-ui/react";
import { color } from "framer-motion";
import { useEffect, useState } from "react";
const ProductCard = ({
  name,
  price,
  uri,
  flowers = null,
  id = 1,
  oldPrice = null,
  discount = null,
  object = {},
  isCart = false,
  num = 0,
}) => {
  const { width } = useWindowDimensions();
  const { pageStore } = useStores();
  const navigate = useNavigate();
  const toast = useToast();
  const [quantity, setQuantity] = useState(num);
  useEffect(() => {
    setQuantity(num);
  }, [num]);

  return (
    <div className={width >= 500 ? styles.container : styles.container375}>
      <Swiper
        onClick={() =>
          navigate("/product", {
            state: { product_id: id, quantity: quantity },
          })
        }
        style={{
          "--swiper-pagination-color": "rgba(237, 237, 237, 1)",
          "--swiper-pagination-bullet-inactive-color": "rgba(131, 131, 131, 1)",
          "--swiper-pagination-bullet-inactive-opacity": "1",
          "--swiper-pagination-bullet-size": "8px",
          "--swiper-pagination-bullet-horizontal-gap": "3px",
        }}
        className={styles.slideTrack}
        modules={[FreeMode, Pagination]}
        spaceBetween={50}
        freeMode={false}
        pagination={true}
      >
        <SwiperSlide className={styles.slider}>
          <img src={uri} alt="" />
        </SwiperSlide>
      </Swiper>
      <p className={styles.nameProductText}>{name}</p>
      <div className={styles.priceView}>
        <p className={styles.priceText}>{price}₽</p>
        {oldPrice && <p className={styles.oldPriceText}>{oldPrice}₽</p>}
        {discount && <p className={styles.discountText}>-{discount}%</p>}
      </div>
      {!isCart ? (
        <p
          className={styles.addButtonText}
          onClick={() => {
            let buffer = Array.from(pageStore.cart);
            buffer.push(object);
            pageStore.updateCart(buffer);
            toast({
              render: () => (
                <VStack
                  color="white"
                  p={3}
                  bg="black"
                  borderRadius={"12px"}
                  border={"2px solid #c81768"}
                >
                  <Text color={"white"}>Букет добавлен в корзину</Text>
                </VStack>
              ),
              duration: 2000,
              isClosable: true,
              position: "bottom",
            });
          }}
        >
          В корзину
        </p>
      ) : (
        <HStack>
          <Text
            color={"white"}
            backgroundColor={"#c81768"}
            padding={"2px 12px"}
            borderRadius={"12px"}
            fontSize={[14, 16]}
            fontWeight={700}
            cursor={"pointer"}
            onClick={() => {
              if (quantity - 1 >= 0) {
                setQuantity(quantity - 1);
                let buffer = Array.from(pageStore.cart);
                buffer.splice(
                  buffer.findIndex((elem) => elem.id == id),
                  1
                );
                pageStore.updateCart(buffer);
              }
            }}
          >
            -
          </Text>
          <Text
            color={"#c81768"}
            padding={"2px 1px"}
            fontSize={20}
            fontWeight={700}
          >
            {quantity}
          </Text>
          <Text
            color={"white"}
            backgroundColor={"#c81768"}
            padding={"2px 12px"}
            borderRadius={"12px"}
            fontSize={[14, 16]}
            fontWeight={700}
            cursor={"pointer"}
            onClick={() => {
              setQuantity(quantity + 1);
              let buffer = Array.from(pageStore.cart);
              buffer.push(object);

              pageStore.updateCart(buffer);
            }}
          >
            +
          </Text>
        </HStack>

        // <p
        //   className={styles.addButtonText}
        //   onClick={() => {
        //     let buffer = Array.from(pageStore.cart);
        //     buffer.splice(
        //       buffer.findIndex((elem) => elem.id == id),
        //       1
        //     );
        //     pageStore.updateCart(buffer);
        //     toast({
        //       duration: 2000,
        //       render: () => (
        //         <VStack color='white' p={3} bg='black' borderRadius={'12px'} border={'2px solid #c81768'}>
        //           <Text color={'white'}>Букет удален из корзины</Text>
        //         </VStack>
        //       ),
        //       isClosable: true,
        //       position: "bottom",
        //     });
        //   }}
        // >
        //   Удалить
        // </p>
      )}
    </div>
  );
};

export default ProductCard;
