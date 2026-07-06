const API = "http://127.0.0.1:8000/finance";

async function fetchTransactions() {
    const res = await fetch(`${API}/all`);
    const data = await res.json();

    const list = document.getElementById("list");
    list.innerHTML = "";

    data.forEach(txn => {
        const li = document.createElement("li");
        li.innerHTML = `
            ${txn.title} - ₹${txn.amount} (${txn.type})
            <button onclick="deleteTxn(${txn.id})">❌</button>
        `;
        list.appendChild(li);
    });
}

async function addTransaction() {
    const txn = {
        title: document.getElementById("title").value,
        amount: parseFloat(document.getElementById("amount").value),
        type: document.getElementById("type").value,
        category: document.getElementById("category").value,
        date: document.getElementById("date").value
    };

    await fetch(`${API}/add`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(txn)
    });

    fetchTransactions();
}

async function deleteTxn(id) {
    await fetch(`${API}/delete/${id}`, { method: "DELETE" });
    fetchTransactions();
}
window.addTransaction = addTransaction;
window.deleteTxn = deleteTxn;
fetchTransactions();