class Battle:
    image.draw(ambrose)
    Ambrose = Player
    Player = turn
    turn = action
    Action
    {ListOfActions:
          action.Punch,
          action.Kick,
          action.Block,
    }

    image.draw(enemy)
    Enemy = Random
    Random = turn
    turn = action
    Action
    {ListOfActions
          action.Punch,
          action.Kick,
          action.Block,
    }

    Enemy = Spawn(random)
