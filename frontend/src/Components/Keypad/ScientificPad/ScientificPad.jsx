import Button from "../../Button/Button";
import './ScientificPad.css'


function ScientificPad({ handleClick,angleMode ,handleMemory}) {
    return (

        <div className="scientific-pad">
            <Button value="sin" onClick={handleClick} />
            <Button value="cos" onClick={handleClick} />
            <Button value="tan" onClick={handleClick} />

            <Button value="asin" onClick={handleClick} />
            <Button value="acos" onClick={handleClick} />
            <Button value="atan" onClick={handleClick} />

            <Button value={angleMode} onClick={handleClick} />

            <Button value="ln" onClick={handleClick} />
            <Button value="log" onClick={handleClick} />
            <Button value="exp" onClick={handleClick} />

            <Button value="sinh" onClick={handleClick} />
            <Button value="cosh" onClick={handleClick} />
            <Button value="tanh" onClick={handleClick} />

            <Button value="nCr" onClick={handleClick} />
            <Button value="nPr" onClick={handleClick} />

            <Button value="asinh" onClick={handleClick} />
            <Button value="acosh" onClick={handleClick} />
            <Button value="atanh" onClick={handleClick} />

            <Button value="√" onClick={handleClick} />
            <Button value="x²" onClick={handleClick} />
            <Button value="x³" onClick={handleClick} />
            <Button value="1/x" onClick={handleClick} />

            <Button value="Ans" onClick={handleClick} />
            <Button value="π" onClick={handleClick} />
            <Button value="e" onClick={handleClick} />
            <Button value="!" onClick={handleClick} />

            <Button value="M+" onClick={() => handleMemory("M+")} />
            <Button value="M-" onClick={() => handleMemory("M-")} />
            <Button value="MR" onClick={() => handleMemory("MR")} />
            <Button value="MC" onClick={() => handleMemory("MC")} />
        </div>

    );
}

export default ScientificPad;
