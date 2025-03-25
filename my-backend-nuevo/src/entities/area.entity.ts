import { Entity, PrimaryGeneratedColumn, Column, NumericType } from 'typeorm';

@Entity()
export class Area {
    @PrimaryGeneratedColumn()
    id :number;

    @Column()
    name: string;
    
}