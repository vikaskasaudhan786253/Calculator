import './Button.css';

function Button({value, onClick}){
    const handleButtonClick = () => {
        console.log("Button clicked:", value);
        onClick(value);
    };
    return(
        <button className="calculator-button"
             onClick={handleButtonClick}>
            {value}
        </button>
    );
}
export default Button;
