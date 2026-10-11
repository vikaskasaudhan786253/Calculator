import "./History.css";

function History({ history, clearHistory,setExpression ,deleteHistory}) {
    return (
        <div className="history">

            <div className="history-header">
                <h3>History</h3>

                {history.length > 0 && (
                    <button
                        className="clear-history-button"
                        onClick={clearHistory}
                    >
                        Clear
                    </button>
                )}
            </div>

            {history.length === 0 ? (
                <p>No calculations yet</p>
            ) : (
                history.map((item, index) => (
                    <div
    className="history-item"
    key={index}
    onClick={() => setExpression(item.expression)}
>
                <div className="history-content">
                    <div className="history-expression">
                        {item.expression}
                    </div>

                    <div className="history-result">
                        = {item.result}
                    </div>
                </div>

                <button
                    className="delete-history-button"
                    onClick={(event) => {
                        event.stopPropagation();
                        deleteHistory(index);
                    }}
                >
                    ✕
                </button>
            </div>
                ))
            )}

        </div>
    );
}

export default History;
