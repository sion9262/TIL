import "./App.css"
import styled from "styled-components";

const Wrapper = styled.section`
  padding: 4em;
  background: papayawhip;
  text-align: center;
`;

const Title = styled.h1`
  font-size: 1.5em;
  text-align: center;
  color: palevioletred;
`;

const Button = styled.button`
  display: inline-block;
  color: palevioletred;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid palevioletred;
  border-radius: 3px;
  display: block;
`;

const TomatoButton = styled(Button)`
  color: tomato;
  border-color: tomato;
`;

const ReversedButton = props => <Button {...props} children={props.children.split('').reverse()} />
function App() {
  return (
    <Wrapper>
      <Title>안녕하세요!</Title>
      <Button>기본</Button>
      <TomatoButton as={ReversedButton}>Tomato is Tomato</TomatoButton>
    </Wrapper>
  );
}
export default App;
