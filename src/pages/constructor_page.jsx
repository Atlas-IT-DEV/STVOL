import {
  VStack,
  Stack,
  Text,
  Image,
  Button,
  HStack,
  Grid,
  GridItem,
} from "@chakra-ui/react";
import { useNavigate } from "react-router";

const ConstructorPage = () => {
  const navigate = useNavigate();
  return (
    <VStack bgColor={"black"} width={"100%"}>
      <Stack
        position={"absolute"}
        right={"10px"}
        top={"10px"}
        bgColor={"white"}
        width={"30px"}
        height={"30px"}
        borderRadius={"50%"}
        alignItems={"center"}
        justifyContent={"center"}
      >
        <Text>✕</Text>
      </Stack>
      <Text color={"white"} fontSize={"80px"}>
        STVOL
      </Text>

      <Text fontSize={30} color={"white"}>
        конструктор
      </Text>

      <VStack width={"60%"} border={"1px solid white"} borderRadius={10}>
        <Image height={"300px"} width={"80%"} marginTop={10} />
        <Button marginTop={5} marginBottom={10}>
          в корзину
        </Button>
      </VStack>
      <HStack marginTop={10}>
        <Button borderRadius={"50%"}>&lt;</Button>
        <Grid
          templateRows="repeat(2, 1fr)"
          templateColumns="repeat(3, 1fr)"
          gap={2}
        >
          <GridItem
            rowSpan={1}
            colSpan={1}
            border={"1px solid white"}
            borderRadius={"10px"}
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
          >
            <Image width={"110px"} height={"110px"} />
          </GridItem>
          <GridItem
            rowSpan={1}
            colSpan={1}
            border={"1px solid white"}
            borderRadius={"10px"}
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
          >
            <Image width={"110px"} height={"110px"} />
          </GridItem>
          <GridItem
            rowSpan={1}
            colSpan={1}
            border={"1px solid white"}
            borderRadius={"10px"}
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
          >
            <Image width={"110px"} height={"110px"} />
          </GridItem>
          <GridItem
            rowSpan={1}
            colSpan={1}
            border={"1px solid white"}
            borderRadius={"10px"}
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
          >
            <Image width={"110px"} height={"110px"} />
          </GridItem>
          <GridItem
            rowSpan={1}
            colSpan={1}
            border={"1px solid white"}
            borderRadius={"10px"}
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
          >
            <Image width={"110px"} height={"110px"} />
          </GridItem>
          <GridItem
            rowSpan={1}
            colSpan={1}
            border={"1px solid white"}
            borderRadius={"10px"}
            display={"flex"}
            justifyContent={"center"}
            alignItems={"center"}
          >
            <Image width={"110px"} height={"110px"} />
          </GridItem>
        </Grid>
        <Button borderRadius={"50%"}>&gt;</Button>
      </HStack>

      <Text marginTop={5} marginBottom={10} color="rgba(215, 215, 215,1)">
        Подсказка: свайпни влево дл того, <br />
        чтобы перейти к настройке букета
      </Text>
    </VStack>
  );
};
export default ConstructorPage;
