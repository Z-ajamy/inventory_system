#library inventory system

classDiagram
    %% Value Objects
    class Money {
        <<Value Object>>
        +Decimal amount
        +Currency currency
        +__add__()
        +__sub__()
    }

    %% Customer
    class Customer {
        <<Entity>>
        +str id
        +str name
        +str phone
    }

    %% Products Hierarchy
    class Product {
        <<Base Entity>>
        +str id
        +ProductFamily type
        +str sku
        +str brand_id
    }
    Product <|-- PenProduct
    Product <|-- RulerProduct
    Product <|-- SchoolBook
    Product <|-- NoteBook

    %% Inventory
    class StockBatch {
        <<Entity>>
        +str id
        +str product_id
        +int current_quantity
        +Money unit_cost
        +Money item_price
        +sell_items(amount)
    }
    StockBatch --> Money : uses

    %% Invoice Aggregate
    class DraftInvoice {
        <<Builder>>
        +str customer_id
        -list _items
        +add_item(batch, quantity)
        +finalize(limit) Invoice
    }

    class InvoiceItem {
        <<Frozen Entity>>
        +str product_id
        +str stock_batch_id
        +int num_of_items
        +Money price_of_item
        +Money price
    }
    
    class Invoice {
        <<Aggregate Root / Frozen>>
        +str id
        +str customer_id
        +tuple items
        +Money total_price
    }

    DraftInvoice ..> Invoice : creates
    DraftInvoice o-- InvoiceItem : gathers
    Invoice *-- InvoiceItem : owns
    InvoiceItem --> Money : uses
