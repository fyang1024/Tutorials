rule numTicketsShouldIncreaseByOne(uint64 ticketPrice, uint16 ticketsAvailable) {
    env e;
    uint16 numTicketsBefore = getNumTickets(e);
    createEvent(e, ticketPrice, ticketsAvailable);
    uint16 numTicketsAfter = getNumTickets(e);
    assert numTicketsAfter == numTicketsBefore + 1, "numTickets did not increase by one";
}

rule numTicketsShouldNeverDecrease(method f) {
    env e;
    calldataarg args;
    uint16 numTicketsBefore = getNumTickets(e);
    f(e, args);
    uint16 numTicketsAfter = getNumTickets(e);
    assert numTicketsAfter >= numTicketsBefore, "numTickets decreased unexpectedly";
}

rule ownerNeverChanges(method f) {
    env e;
    calldataarg args;
    address ownerBefore = owner(e);
    f(e, args);
    address ownerAfter = owner(e);
    assert ownerBefore == ownerAfter, "owner changed unexpectedly";
}

rule transactionFeeNeverChanges(method f) {
    env e;
    calldataarg args;
    uint64 transactionFeeBefore = transactionFee(e);
    f(e, args);
    uint64 transactionFeeAfter = transactionFee(e);
    assert transactionFeeBefore == transactionFeeAfter, "transactionFee changed unexpectedly";
}

rule buyNewTicketFromEventWithEnoughTickets(uint16 eventID, address attendee) {
    env e;
    uint16 ticketsRemaining = ticketsRemaining(e, eventID);
    uint16 ticketID = buyNewTicket(e, eventID, attendee);
    assert ticketID !=0 => ticketsRemaining > 0, "event has no tickets available";
}