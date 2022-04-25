import "./App.css"
import styled from "styled-components";

const Button = styled.button`
  box-sizing: border-box;
  margin: 10px;
  padding: 15px 30px;
  border-radius: 15px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
  background-color: ${props => props.bgColor};
  color: ${props => props.color};
`;

function App() {
  return (
    <div>
      <button className="button button--color-white">하얀색</button>
      <button className="button button--color-black">검은색</button>
      <div>
        <Button bgColor="white" color="black">하얀색</Button>
        <Button bgColor="red" color="white">빨간색</Button>
        <Button bgColor="black" color="white">검은색</Button>
      </div>
    </div>
  );
}
export default App;
