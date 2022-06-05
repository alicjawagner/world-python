import random
#import World

class Organism:

    DELIMITER = " "

    def __init__(self, _world):
        self.world = _world
        self.strength = -1
        self.initiative = -1
        self.isAlive = True
        self.stepRange = 1
        self.birthTime = self.world.numberOfBornOrganisms + 1

        int x, y
        int fields = World.FIELDS_NUMBER
        do {
            x = rand.nextInt(fields)
            y = rand.nextInt(fields)
        } while (world.board[x][y] != null)

        point.x = x
        point.y = y
    

    public Organism(World _world, String[] arr) {
        world = _world
        isAlive = true
        stepRange = 1
        point.x = Integer.parseInt(arr[1])
        point.y = Integer.parseInt(arr[2])
        birthTime = Integer.parseInt(arr[3])
        strength = Integer.parseInt(arr[4])
    }

    public abstract OrganismsNames whoAmI()
    public abstract void action()
    public abstract void draw(Graphics g)

    public String getName() {
        return name
    }

    public int getStrength() {
        return strength
    }

    public int getInitiative() {
        return initiative
    }

    public Point getPoint() {
        return point
    }

    public boolean getIsAlive() {
        return isAlive
    }

    public World getWorld() {
        return world
    }

    public void setStrength(final int newStrength) {
        strength = newStrength
    }

    public void setBirthTime(final int _birthTime) {
        birthTime = _birthTime
    }

    protected enum Strength {
        STRONGER,
        EQUAL,
        WEAKER
    }

    protected Strength amIStronger(final Organism other) {
        if (strength > other.strength) return Strength.STRONGER
   	    else if (strength == other.strength) return Strength.EQUAL
   	    else return Strength.WEAKER
    }

    public boolean ifIRepelledTheAttack(final Organism attacker) {
        return false
    }

    public boolean ifIEscaped(Animal attacker) {
        return false
    }

    public boolean ifILostTheFight(Organism attacker) {
        return amIStronger(attacker) != Strength.STRONGER
    }

    public ArrayList < Point > findFieldsToMove() {
        Point current, possibleMove
        current = point

        ArrayList < Point > possibleMoves = new ArrayList <> ()
        for (int i=-1 * stepRange
             i <= stepRange
             i += stepRange) {
            for (int j=-1 * stepRange
                 j <= stepRange
                 j += stepRange) {
                if (i == 0 & & j == 0)
                continue

                possibleMove = new Point(current.x + i, current.y + j)
                if (world.isFieldInBoard(possibleMove))
                possibleMoves.add(possibleMove)
            }
        }

        return possibleMoves
    }

    public void removeOccupiedFields(ArrayList < Point > possibleMoves) {
        possibleMoves.removeIf(field -> (!world.isFieldUnoccupied(field)))
    }

    public void putOnBoard() {
        world.board[point.x][point.y] = this
    }

    public void moveToField(Point newPoint) {
        world.clearTheField(point)
        point = newPoint
        putOnBoard()
    }

    public void writeIWon() {
        world.text += this + " won the fight: "
    }

    public void writeIDie() {
        world.text += name + " is dead :(\n"
    }

    public void die() {
        isAlive = false
        world.clearTheField(point)
        writeIDie()
    }

    public void makeChild(ArrayList < Point > possibleFields) {
        Organism child = world.createOrganism(this.whoAmI())

        int which = rand.nextInt(possibleFields.size())
        child.moveToField(possibleFields.get(which))
        world.insertIntoToAdd(child)
    }

    protected abstract void drawShapeOrg(Graphics g, Color color)

    protected void drawOrg(Graphics g, Color color) {
        drawShapeOrg(g, color)

        g.setColor(Color.white)
        g.setFont(new Font("Helvetica", Font.BOLD, 25))
        FontMetrics metrics = world.getFontMetrics(g.getFont())
        double x = ((double)(2 * point.x + 1) * FIELD_SIZE) / 2
        double y = ((double)(2 * point.y + 2) * FIELD_SIZE) / 2
        g.drawString(sign, (int)(x - (metrics.stringWidth(sign) / 2)),
                     (int)(y - (g.getFont().getSize() / 2)) + 4)
    }

    @ Override
    public String toString() {
        return name + " (" + point.x + "," + point.y + ")"
    }

    public void writeMeToFile(BufferedWriter writer) throws IOException {
        writer.write(sign + DELIMITER + point.x + DELIMITER +
                     point.y + DELIMITER + birthTime + DELIMITER + strength)
        myOwnFieldsToFile(writer)
        writer.newLine()
    }

    protected void myOwnFieldsToFile(BufferedWriter writer) throws IOException {
    }
